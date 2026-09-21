from flask import Blueprint, request, jsonify
from flask_login import current_user, login_user
from models import db
from models.symptom import Symptom
from models.disease_rule import Disease
from models.diagnosis_case import DiagnosisCase
from models.user import User
from routes.diagnosis import forward_chaining
from translations import get_localized_symptom, get_localized_disease
import json

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint for frontend to ping"""
    return jsonify({
        'status': 'healthy',
        'app': 'Coffee Disease Expert System API',
        'version': '1.0.0'
    })

@api_bp.route('/symptoms', methods=['GET'])
def get_symptoms():
    """Returns list of symptoms for the frontend UI"""
    lang = request.args.get('lang', 'km')
    symptoms = Symptom.query.order_by(Symptom.id.asc()).all()
    data = []
    for s in symptoms:
        loc = get_localized_symptom(s, lang=lang)
        data.append({
            'id': s.id,
            'code': s.code,
            'name': loc['name'],
            'description': loc['description'],
            'category': s.category
        })
    return jsonify({
        'success': True,
        'count': len(data),
        'symptoms': data
    })

@api_bp.route('/diseases', methods=['GET'])
def get_diseases():
    """Returns list of coffee diseases"""
    lang = request.args.get('lang', 'km')
    diseases = Disease.query.order_by(Disease.id.asc()).all()
    data = []
    for d in diseases:
        loc = get_localized_disease(d, lang=lang)
        data.append({
            'id': d.id,
            'code': d.code,
            'name': loc['name'],
            'scientific_name': d.scientific_name,
            'severity': d.severity,
            'description': loc['description'],
            'treatment': loc['treatment'],
            'prevention': loc['prevention']
        })
    return jsonify({
        'success': True,
        'count': len(data),
        'diseases': data
    })

@api_bp.route('/diagnose', methods=['POST'])
def diagnose():
    """Inference diagnosis endpoint callable from any frontend (React, Next.js, Mobile)"""
    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    symptom_ids = payload.get('symptoms', [])
    if isinstance(symptom_ids, str):
        try:
            symptom_ids = json.loads(symptom_ids)
        except Exception:
            symptom_ids = [s.strip() for s in symptom_ids.split(',') if s.strip()]

    location = payload.get('location', '')
    notes = payload.get('notes', '')

    if not symptom_ids:
        return jsonify({'success': False, 'error': 'No symptoms selected'}), 400

    results = forward_chaining(symptom_ids)

    case_id = None
    if current_user.is_authenticated:
        case = DiagnosisCase(
            user_id=current_user.id,
            symptoms_selected=json.dumps(symptom_ids),
            diagnosis_result=json.dumps(results),
            confidence_score=results[0]['confidence'] if results else 0,
            disease_diagnosed=results[0]['disease_name'] if results else 'Unknown',
            location=location,
            notes=notes
        )
        db.session.add(case)
        db.session.commit()
        case_id = case.id

    return jsonify({
        'success': True,
        'case_id': case_id,
        'results': results
    })

@api_bp.route('/auth/login', methods=['POST'])
def api_login():
    """JSON login endpoint for external frontends"""
    payload = request.get_json(silent=True) or {}
    username = payload.get('username')
    password = payload.get('password')

    if not username or not password:
        return jsonify({'success': False, 'error': 'Username and password required'}), 400

    user = User.query.filter((User.username == username) | (User.email == username)).first()
    if user and user.check_password(password):
        login_user(user, remember=True)
        return jsonify({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': user.full_name,
                'role': user.role
            }
        })
    return jsonify({'success': False, 'error': 'Invalid username or password'}), 401
