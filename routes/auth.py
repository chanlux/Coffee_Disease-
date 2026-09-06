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
        identifier = request.form.get('username')  
        password = request.form.get('password')
        
        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('diagnosis.dashboard'))
        else:
            flash('ព័ត៌មានចូលមិនត្រឹមត្រូវ', 'danger')
    return render_template('login.html')

@auth_bp.route('/manage-users')
@login_required
def manage_users():
    if current_user.role != 'admin':
        flash('ការចូលប្រើត្រូវបានបដិសេធ។', 'danger')
        return redirect(url_for('diagnosis.dashboard'))
    
    users = User.query.all()
    return render_template('manager_users.html', users=users)

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
        user.full_name = request.form.get('full_name')
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
        full_name = request.form.get('name') 
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

@auth_bp.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('អ្នកបានចាកចេញរួចហើយ', 'info')
    return redirect(url_for('auth.login'))