from flask import Flask
import os
import json
from config import Config, config as config_dict
from models import db, login_manager, init_app
from routes import register_routes


def create_app(config_class=None):
    app = Flask(__name__)

    # Force production configuration on Vercel so it reads DATABASE_URL
    if config_class is None:
        env = os.environ.get('FLASK_ENV', 'production')
        config_class = config_dict.get(env, Config)

    app.config.from_object(config_class)

    # Wrap folder creation in try-except so read-only serverless environments don't crash
    try:
        os.makedirs('database', exist_ok=True)
        os.makedirs('static/images/coffee_leaves', exist_ok=True)
    except OSError:
        pass

    init_app(app)

    def from_json_filter(value):
        try:
            if isinstance(value, str):
                return json.loads(value)
            return value if value else []
        except (json.JSONDecodeError, TypeError):
            return []

    app.jinja_env.filters['from_json'] = from_json_filter

    CATEGORY_KM = {
        'leaf': 'ស្លឹក',
        'berry': 'ផ្លែ',
        'root': 'ឫស',
        'stem': 'ដើម',
        'other': 'ផ្សេងៗ',
    }

    SEVERITY_KM = {
        'low': 'ស្រាល',
        'medium': 'មធ្យម',
        'high': 'ខ្ពស់',
        'critical': 'ធ្ងន់ធ្ងរបំផុត',
    }

    def category_km_filter(value):
        if not value:
            return value
        return CATEGORY_KM.get(str(value).lower(), value)

    def severity_km_filter(value):
        if not value:
            return value
        return SEVERITY_KM.get(str(value).lower(), value)

    app.jinja_env.filters['category_km'] = category_km_filter
    app.jinja_env.filters['severity_km'] = severity_km_filter

    register_routes(app)

    # Safely handle database creation and sample data population on startup
    with app.app_context():
        try:
            db.create_all()
            create_sample_data()
        except Exception as e:
            # Prevents app crash on Vercel if remote DB is unreachable or already initialized
            print(f"Database initialization warning: {e}")

    return app


def create_sample_data():
    """Create sample data if database is empty"""

    from models.user import User
    from models.symptom import Symptom
    from models.disease_rule import Disease, DiseaseRule

    try:
        if User.query.count() == 0:
            admin = User(
                username='admin',
                email='admin@coffee.com',
                full_name='អ្នកគ្រប់គ្រងប្រព័ន្ធ',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)

            user = User(
                username='user',
                email='user@coffee.com',
                full_name='អ្នកចូលមើលគេហទំព័រ',
                role='user'
            )
            user.set_password('user123')
            db.session.add(user)

            doctor = User(
                username='doctor',
                email='doctor@coffee.com',
                full_name='វេជ្ជបណ្ឌិត អ្នកជំនាញកាហ្វេ',
                role='doctor'
            )
            doctor.set_password('doctor123')
            db.session.add(doctor)

        if Symptom.query.count() == 0:
            symptoms_data = [
                {'code': 'S01', 'name': 'ចំណុចលឿងនៅលើស្លឹក', 'category': 'leaf'},
                {'code': 'S02', 'name': 'របួសពណ៌ត្នោត', 'category': 'leaf'},
                {'code': 'S03', 'name': 'ស្លឹកទន់ស្រពោន', 'category': 'leaf'},
                {'code': 'S04', 'name': 'ស្រទាប់សដូចម្សៅ', 'category': 'leaf'},
                {'code': 'S05', 'name': 'ស្លឹកជ្រុះមុនកំណត់', 'category': 'leaf'},
            ]

            for s in symptoms_data:
                symptom = Symptom(**s)
                db.session.add(symptom)

        if Disease.query.count() == 0:
            diseases_data = [
                {
                    'code': 'D01',
                    'name': 'ជំងឺច្រែះស្លឹកកាហ្វេ',
                    'scientific_name': 'Hemileia vastatrix',
                    'description': 'ជំងឺផ្សិតដែលប៉ះពាល់ដល់ស្លឹកកាហ្វេ',
                    'treatment': 'ប្រើថ្នាំសម្លាប់ផ្សិតដែលមានផ្អែកលើទង់ដែង',
                    'prevention': 'កាត់មែកឈើដែលឆ្លងជំងឺ និងកែលម្អចរន្តខ្យល់',
                    'severity': 'high'
                },
                {
                    'code': 'D02',
                    'name': 'ជំងឺផ្លែកាហ្វេ',
                    'scientific_name': 'Colletotrichum kahawae',
                    'description': 'ប៉ះពាល់ដល់ផ្លែកាហ្វេ',
                    'treatment': 'ដកផ្លែកាហ្វេដែលឆ្លងជំងឺចេញ ហើយប្រើថ្នាំសម្លាប់ផ្សិត',
                    'prevention': 'ត្រួតពិនិត្យជាទៀងទាត់ និងអនាម័យ',
                    'severity': 'critical'
                }
            ]

            for d in diseases_data:
                disease = Disease(**d)
                db.session.add(disease)

        db.session.commit()

        if DiseaseRule.query.count() == 0:
            rules_data = [
                {'disease_id': 1, 'symptom_id': 1, 'certainty_factor': 0.9, 'weight': 1.0},
                {'disease_id': 1, 'symptom_id': 2, 'certainty_factor': 0.8, 'weight': 0.8},
                {'disease_id': 2, 'symptom_id': 2, 'certainty_factor': 0.85, 'weight': 0.9},
                {'disease_id': 2, 'symptom_id': 3, 'certainty_factor': 0.75, 'weight': 0.7},
            ]

            for r in rules_data:
                rule = DiseaseRule(**r)
                db.session.add(rule)

            db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Sample data creation skipped: {e}")




app = create_app()

# Run locally
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )