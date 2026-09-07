from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db
from models.diagnosis_case import DiagnosisCase
from datetime import datetime, timedelta
import json

cases_bp = Blueprint('cases', __name__, url_prefix='/cases')

@cases_bp.route('/')
@login_required
def index():
    period = request.args.get('period')
    
    if current_user.role in ['admin', 'manager', 'expert']:
        query = DiagnosisCase.query
    else:
        query = DiagnosisCase.query.filter_by(user_id=current_user.id)

    if period:
        now = datetime.utcnow()
        if period == 'today':
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            query = query.filter(DiagnosisCase.created_at >= start)
        elif period == 'week':
            start = now - timedelta(days=7)
            query = query.filter(DiagnosisCase.created_at >= start)
        elif period == 'month':
            start = now - timedelta(days=30)
            query = query.filter(DiagnosisCase.created_at >= start)

    cases = query.order_by(DiagnosisCase.created_at.desc()).all()
    return render_template('cases_history.html', cases=cases, active_period=period)

@cases_bp.route('/<int:case_id>')
@login_required
def view_case(case_id):
    case = DiagnosisCase.query.get_or_404(case_id)
    if current_user.role not in ['admin', 'manager', 'expert'] and case.user_id != current_user.id:
        return jsonify({'error': 'គ្មានការអនុញ្ញាត'}), 403

    try:
        diag_res = json.loads(case.diagnosis_result) if case.diagnosis_result else []
    except Exception:
        diag_res = []

    try:
        symptoms_sel = json.loads(case.symptoms_selected) if case.symptoms_selected else []
    except Exception:
        symptoms_sel = []

    if request.headers.get('Accept') == 'application/json' or request.is_json:
        return jsonify({
            'id': case.id,
            'disease_diagnosed': case.disease_diagnosed,
            'confidence_score': case.confidence_score,
            'location': case.location,
            'notes': case.notes,
            'created_at': case.created_at.strftime('%Y-%m-%d %H:%M') if case.created_at else '',
            'diagnosis_result': diag_res,
            'symptoms_selected': symptoms_sel
        })

    return render_template('cases_history.html', cases=[case], active_period=None)


@cases_bp.route('/<int:case_id>/delete', methods=['POST'])
@login_required
def delete_case(case_id):
    if current_user.role not in ['admin', 'manager']:
        return jsonify({'success': False, 'message': 'គ្មានការអនុញ្ញាត'}), 403
    
    case = DiagnosisCase.query.get_or_404(case_id)
    try:
        db.session.delete(case)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})
    