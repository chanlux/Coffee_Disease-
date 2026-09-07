from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    
    from models.user import User
    from models.symptom import Symptom
    from models.disease_rule import Disease, DiseaseRule
    from models.diagnosis_case import DiagnosisCase
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))