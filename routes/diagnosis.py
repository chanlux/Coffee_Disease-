from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models import db
from models.symptom import Symptom
from models.disease_rule import Disease, DiseaseRule
from models.diagnosis_case import DiagnosisCase
import json
from collections import defaultdict

diagnosis_bp = Blueprint('diagnosis', __name__, url_prefix='/diagnosis')

@diagnosis_bp.route('/dashboard')
@login_required
def dashboard():
    from datetime import datetime
    from sqlalchemy import func

    is_admin_or_expert = current_user.role in ['admin', 'manager', 'expert', 'doctor']
    start_of_month = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    if is_admin_or_expert:
        total_cases = DiagnosisCase.query.count()
        month_cases = DiagnosisCase.query.filter(DiagnosisCase.created_at >= start_of_month).count()
        recent_cases = DiagnosisCase.query.order_by(DiagnosisCase.created_at.desc()).limit(5).all()
        avg_conf = db.session.query(func.avg(DiagnosisCase.confidence_score)).scalar() or 0
    else:
        total_cases = DiagnosisCase.query.filter_by(user_id=current_user.id).count()
        month_cases = DiagnosisCase.query.filter_by(user_id=current_user.id).filter(DiagnosisCase.created_at >= start_of_month).count()
        recent_cases = DiagnosisCase.query.filter_by(user_id=current_user.id).order_by(DiagnosisCase.created_at.desc()).limit(5).all()
        avg_conf = db.session.query(func.avg(DiagnosisCase.confidence_score)).filter(DiagnosisCase.user_id == current_user.id).scalar() or 0

    avg_confidence = round(float(avg_conf), 1)
    total_diseases = Disease.query.count()
    total_symptoms = Symptom.query.count()

    return render_template('dashboard.html', 
                           total_cases=total_cases, 
                           recent_cases=recent_cases,
                           month_cases=month_cases,
                           avg_confidence=avg_confidence,
                           total_diseases=total_diseases,
                           total_symptoms=total_symptoms,
                           is_admin_view=is_admin_or_expert)

@diagnosis_bp.route('/diagnose', methods=['GET', 'POST'])
@login_required
def diagnose():
    if request.method == 'GET':
        symptoms = Symptom.query.all()
        return render_template('diagnosis.html', symptoms=symptoms)
    
    if request.is_json:
        payload = request.get_json() or {}
        selected_symptoms = payload.get('symptoms', [])
        location = payload.get('location', '')
        notes = payload.get('notes', '')
    else:
        selected_symptoms = request.form.getlist('symptoms[]')
        location = request.form.get('location', '')
        notes = request.form.get('notes', '')
    
    if not selected_symptoms:
        return jsonify({'error': 'មិនបានជ្រើសរើសរោគសញ្ញា / No symptoms selected'}), 400

    results = forward_chaining(selected_symptoms)
    
    case = DiagnosisCase(
        user_id=current_user.id,
        symptoms_selected=json.dumps(selected_symptoms),
        diagnosis_result=json.dumps(results),
        confidence_score=results[0]['confidence'] if results else 0,
        disease_diagnosed=results[0]['disease_name'] if results else 'Unknown',
        location=location,
        notes=notes
    )
    
    db.session.add(case)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'case_id': case.id,
        'results': results
    })

def forward_chaining(symptom_ids):
    """
    Forward chaining inference algorithm
    Calculates disease probability based on symptoms
    """
    symptom_ids = [int(sid) for sid in symptom_ids]
    
    rules = DiseaseRule.query.filter(
        DiseaseRule.symptom_id.in_(symptom_ids)
    ).all()
    
    disease_scores = defaultdict(lambda: {'total': 0, 'count': 0, 'disease': None})
    
    for rule in rules:
        disease_id = rule.disease_id
        disease_scores[disease_id]['total'] += rule.certainty_factor * rule.weight
        disease_scores[disease_id]['count'] += 1
        disease_scores[disease_id]['disease'] = rule.disease
    
    from translations import DISEASE_TRANSLATIONS_EN

    results = []
    for disease_id, data in disease_scores.items():
        disease = data['disease']
        confidence = (data['total'] / data['count']) * 100
        en_info = DISEASE_TRANSLATIONS_EN.get(disease.code, {})
        
        results.append({
            'disease_id': disease_id,
            'disease_name': disease.name,
            'disease_name_en': en_info.get('name', disease.name),
            'disease_code': disease.code,
            'scientific_name': disease.scientific_name,
            'confidence': round(confidence, 2),
            'severity': disease.severity,
            'description': disease.description,
            'description_en': en_info.get('description', disease.description),
            'treatment': disease.treatment,
            'treatment_en': en_info.get('treatment', disease.treatment),
            'prevention': disease.prevention,
            'prevention_en': en_info.get('prevention', disease.prevention),
            'matched_symptoms': data['count']
        })
    
    results.sort(key=lambda x: x['confidence'], reverse=True)
    
    return results