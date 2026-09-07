from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.disease_rule import Disease, DiseaseRule
from models.symptom import Symptom

rules_bp = Blueprint('rules', __name__, url_prefix='/rules')

@rules_bp.route('/')
@rules_bp.route('/rules/')
@login_required
def index():
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        flash('គ្មានសិទ្ធិចូលប្រើ', 'danger')
        return redirect(url_for('diagnosis.dashboard'))
        
    diseases = Disease.query.all()
    symptoms = Symptom.query.all()
    rules = DiseaseRule.query.all()    
    
    return render_template('rules_management.html', 
                          diseases=diseases, 
                          symptoms=symptoms,
                          rules=rules)

@rules_bp.route('/disease/add', methods=['POST'])
@login_required
def add_disease():
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        flash('គ្មានសិទ្ធិចូលប្រើ', 'danger')
        return redirect(url_for('rules.index'))
    
    disease = Disease(
        code=request.form.get('code'),
        name=request.form.get('name'),
        scientific_name=request.form.get('scientific_name'),
        description=request.form.get('description'),
        treatment=request.form.get('treatment'),
        prevention=request.form.get('prevention'),
        severity=request.form.get('severity')
    )
    
    db.session.add(disease)
    db.session.commit()
    
    flash('បានបន្ថែមជំងឺដោយជោគជ័យ', 'success')
    return redirect(url_for('rules.index'))

@rules_bp.route('/disease/<int:disease_id>/edit', methods=['POST'])
@login_required
def edit_disease(disease_id):
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403
    
    disease = Disease.query.get_or_404(disease_id)
    
    disease.code = request.form.get('code')
    disease.name = request.form.get('name')
    disease.scientific_name = request.form.get('scientific_name')
    disease.description = request.form.get('description')
    disease.treatment = request.form.get('treatment')
    disease.prevention = request.form.get('prevention')
    disease.severity = request.form.get('severity')
    
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'បានធ្វើបច្ចុប្បន្នភាពជំងឺ'})

@rules_bp.route('/disease/<int:disease_id>/delete', methods=['POST'])
@login_required
def delete_disease(disease_id):
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403
    
    disease = Disease.query.get_or_404(disease_id)
    db.session.delete(disease)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'បានលុបជំងឺ'})

@rules_bp.route('/rule/add', methods=['POST'])
@login_required
def add_rule():
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403
    
    rule = DiseaseRule(
        disease_id=request.form.get('disease_id'),
        symptom_id=request.form.get('symptom_id'),
        certainty_factor=float(request.form.get('certainty_factor', 1.0)),
        weight=float(request.form.get('weight', 1.0))
    )
    
    db.session.add(rule)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'បានបន្ថែមច្បាប់'})

@rules_bp.route('/symptom/add', methods=['POST'])
@login_required
def add_symptom():
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403
    
    symptom = Symptom(
        code=request.form.get('code'),
        name=request.form.get('name'),
        description=request.form.get('description'),
        category=request.form.get('category')
    )
    
    db.session.add(symptom)
    db.session.commit()
    
    flash('បានបន្ថែមរោគសញ្ញាដោយជោគជ័យ', 'success')
    return redirect(url_for('rules.index'))

@rules_bp.route('/symptom/<int:symptom_id>/edit', methods=['POST'])
@login_required
def edit_symptom(symptom_id):
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403

    symptom = Symptom.query.get_or_404(symptom_id)

    symptom.code = request.form.get('code')
    symptom.name = request.form.get('name')
    symptom.description = request.form.get('description')
    symptom.category = request.form.get('category')

    db.session.commit()

    return jsonify({'success': True, 'message': 'បានធ្វើបច្ចុប្បន្នភាពរោគសញ្ញា'})

@rules_bp.route('/symptom/<int:symptom_id>/delete', methods=['POST'])
@login_required
def delete_symptom(symptom_id):
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403

    symptom = Symptom.query.get_or_404(symptom_id)
    db.session.delete(symptom)
    db.session.commit()

    return jsonify({'success': True, 'message': 'បានលុបរោគសញ្ញា'})

@rules_bp.route('/rule/<int:rule_id>/delete', methods=['POST'])
@login_required
def delete_rule(rule_id):
    if current_user.role not in ['admin', 'expert', 'manager', 'doctor']:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403

    rule = DiseaseRule.query.get_or_404(rule_id)
    db.session.delete(rule)
    db.session.commit()

    return jsonify({'success': True, 'message': 'បានលុបច្បាប់'})
