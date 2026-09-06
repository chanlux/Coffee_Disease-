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
def dashboard():
    
    total_cases = DiagnosisCase.query.count()    
    recent_cases = DiagnosisCase.query.order_by(DiagnosisCase.created_at.desc()).limit(5).all()    
    
    return render_template('dashboard.html', 
                           total_cases=total_cases, 
                           recent_cases=recent_cases)

@diagnosis_bp.route('/diagnose', methods=['GET', 'POST'])
@login_required
def diagnose():
    if request.method == 'GET':
        symptoms = Symptom.query.all()
        return render_template('diagnosis.html', symptoms=symptoms)
    
    selected_symptoms = request.form.getlist('symptoms[]')
    
    if not selected_symptoms:
        return jsonify({'error': 'មិនបានជ្រើសរើសរោគសញ្ញា'}), 400

    results = forward_chaining(selected_symptoms)
    
    case = DiagnosisCase(
        user_id=current_user.id,
        symptoms_selected=json.dumps(selected_symptoms),
        diagnosis_result=json.dumps(results),
        confidence_score=results[0]['confidence'] if results else 0,
        disease_diagnosed=results[0]['disease_name'] if results else 'Unknown',
        location=request.form.get('location', ''),
        notes=request.form.get('notes', '')
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
    
    results = []
    for disease_id, data in disease_scores.items():
        disease = data['disease']
        confidence = (data['total'] / data['count']) * 100
        
        results.append({
            'disease_id': disease_id,
            'disease_name': disease.name,
            'disease_code': disease.code,
            'confidence': round(confidence, 2),
            'severity': disease.severity,
            'description': disease.description,
            'treatment': disease.treatment,
            'prevention': disease.prevention,
            'matched_symptoms': data['count']
        })
    
    results.sort(key=lambda x: x['confidence'], reverse=True)
    
    return results