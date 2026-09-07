from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db
from models.user import User
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('diagnosis.dashboard'))
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('diagnosis.dashboard'))
        
    if request.method == 'POST':
        login_input = request.form.get('username')
        password = request.form.get('password')
        remember = bool(request.form.get('remember'))
        
        user = User.query.filter((User.username == login_input) | (User.email == login_input)).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            flash(f'សូមស្វាគមន៍មកកាន់ប្រព័ន្ធ, {user.full_name or user.username}!', 'success')
            return redirect(next_page or url_for('diagnosis.dashboard'))
        else:
            flash('ឈ្មោះអ្នកប្រើប្រាស់/អ៊ីមែល ឬពាក្យសម្ងាត់មិនត្រឹមត្រូវទេ', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/dashboard')
def dashboard_redirect():
    return redirect(url_for('diagnosis.dashboard'))

@auth_bp.route('/manage-users')
@auth_bp.route('/users')
@login_required
def manage_users():
    if current_user.role != 'admin':
        flash('ការចូលប្រើត្រូវបានបដិសេធ។', 'danger')
        return redirect(url_for('diagnosis.dashboard'))
    
    users = User.query.order_by(User.id.asc()).all()
    return render_template('manager_users.html', users=users)

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    from models.diagnosis_case import DiagnosisCase
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if email and email != current_user.email:
            existing = User.query.filter_by(email=email).first()
            if existing and existing.id != current_user.id:
                flash('អ៊ីមែលនេះត្រូវបានប្រើប្រាស់ដោយគណនីផ្សេងរួចហើយ!', 'danger')
                return redirect(url_for('auth.profile'))
            current_user.email = email

        if full_name is not None:
            current_user.full_name = full_name

        if new_password:
            if not current_password or not current_user.check_password(current_password):
                flash('ពាក្យសម្ងាត់បច្ចុប្បន្នមិនត្រឹមត្រូវទេ!', 'danger')
                return redirect(url_for('auth.profile'))
            if new_password != confirm_password:
                flash('ពាក្យសម្ងាត់ថ្មី និងការបញ្ជាក់ពាក្យសម្ងាត់មិនត្រូវគ្នាទេ!', 'danger')
                return redirect(url_for('auth.profile'))
            if len(new_password) < 6:
                flash('ពាក្យសម្ងាត់ថ្មីត្រូវមានយ៉ាងតិច ៦ តួអក្សរ!', 'danger')
                return redirect(url_for('auth.profile'))
            current_user.set_password(new_password)

        try:
            db.session.commit()
            flash('ព័ត៌មានគណនីរបស់អ្នកត្រូវបានធ្វើបច្ចុប្បន្នភាពដោយជោគជ័យ!', 'success')
            return redirect(url_for('auth.profile'))
        except Exception as e:
            db.session.rollback()
            flash(f'កំហុសក្នុងការធ្វើបច្ចុប្បន្នភាព៖ {str(e)}', 'danger')

    user_cases_count = DiagnosisCase.query.filter_by(user_id=current_user.id).count()
    return render_template('profile.html', user_cases_count=user_cases_count)

@auth_bp.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        flash('គ្មានសិទ្ធិចូលប្រើ', 'danger')
        return redirect(url_for('diagnosis.dashboard'))

    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        new_full_name = request.form.get('full_name')
        if new_full_name is not None:
            user.full_name = new_full_name
        user.role = request.form.get('role')
        
        try:
            db.session.commit()
            flash('បានធ្វើបច្ចុប្បន្នភាពអ្នកប្រើប្រាស់ដោយជោគជ័យ', 'success')
            return redirect(url_for('auth.manage_users'))
        except Exception as e:
            db.session.rollback()
            flash(f'កំហុសក្នុងការធ្វើបច្ចុប្បន្នភាពអ្នកប្រើប្រាស់៖ {str(e)}', 'danger')

    return render_template('edit_user.html', user=user)

@auth_bp.route('/user/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role == 'admin':
        user = User.query.get_or_404(user_id)
        if user.id == current_user.id:
            flash('អ្នកមិនអាចលុបខ្លួនឯងបានទេ!', 'warning')
        else:
            db.session.delete(user)
            db.session.commit()
            flash('បានលុបអ្នកប្រើប្រាស់ដោយជោគជ័យ។', 'success')
    else:
        flash('សកម្មភាពគ្មានការអនុញ្ញាត។', 'danger')
        
    return redirect(url_for('auth.manage_users'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username') 
        full_name = request.form.get('full_name') or request.form.get('name') or username
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash('ឈ្មោះអ្នកប្រើប្រាស់នេះត្រូវបានប្រើរួចហើយ', 'danger')
            return redirect(url_for('auth.register'))
            
        if User.query.filter_by(email=email).first():
            flash('អ៊ីមែលនេះត្រូវបានចុះឈ្មោះរួចហើយ', 'danger')
            return redirect(url_for('auth.register'))

        user = User(username=username, email=email, full_name=full_name, role='user')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('ការចុះឈ្មោះជោគជ័យ! សូមចូលប្រើប្រាស់។', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        flash('ប្រសិនបើអ៊ីមែលនេះមានក្នុងប្រព័ន្ធ តំណកំណត់ពាក្យសម្ងាត់ឡើងវិញត្រូវបានផ្ញើជូនហើយ។', 'info')
        return redirect(url_for('auth.login'))
    return render_template('forgot_password.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('អ្នកបានចាកចេញរួចហើយ', 'info')
    return redirect(url_for('auth.login'))