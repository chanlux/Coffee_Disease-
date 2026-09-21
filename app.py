from flask import Flask
import os
import json
from config import Config, config as config_dict
from models import db, login_manager, init_app
from routes import register_routes


def create_app(config_class=None):
    app = Flask(__name__)

    # Default to production on Vercel or Render, and development when running locally
    if config_class is None:
        default_env = 'production' if (os.environ.get('VERCEL') == '1' or os.environ.get('RENDER')) else 'development'
        env = os.environ.get('FLASK_ENV', default_env)
        config_class = config_dict.get(env, Config)
    elif isinstance(config_class, str):
        config_class = config_dict.get(config_class, Config)

    app.config.from_object(config_class)

    # Enable ProxyFix behind reverse proxies (Render, Vercel)
    if os.environ.get('RENDER') or os.environ.get('VERCEL') == '1':
        try:
            from werkzeug.middleware.proxy_fix import ProxyFix
            app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
        except Exception:
            pass

    # Ensure static upload directory exists
    try:
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

    from flask import session, request, redirect, url_for
    from translations import gettext, get_localized_symptom, get_localized_disease

    CATEGORY_MAP = {
        'km': {'leaf': 'ស្លឹក', 'berry': 'ផ្លែ', 'root': 'ឫស', 'stem': 'ដើម & មែក', 'other': 'ផ្សេងៗ'},
        'en': {'leaf': 'Leaf', 'berry': 'Berry', 'root': 'Root', 'stem': 'Stem & Branch', 'other': 'Other'}
    }

    SEVERITY_MAP = {
        'km': {'low': 'ស្រាល', 'medium': 'មធ្យម', 'high': 'ខ្ពស់', 'critical': 'ធ្ងន់ធ្ងរបំផុត'},
        'en': {'low': 'Low', 'medium': 'Medium', 'high': 'High', 'critical': 'Critical'}
    }

    def category_filter(value):
        if not value:
            return value
        lang = session.get('lang', 'km')
        mapping = CATEGORY_MAP.get(lang, CATEGORY_MAP['km'])
        return mapping.get(str(value).lower(), value)

    def severity_filter(value):
        if not value:
            return value
        lang = session.get('lang', 'km')
        mapping = SEVERITY_MAP.get(lang, SEVERITY_MAP['km'])
        return mapping.get(str(value).lower(), value)

    app.jinja_env.filters['category_km'] = category_filter
    app.jinja_env.filters['severity_km'] = severity_filter
    app.jinja_env.filters['category_label'] = category_filter
    app.jinja_env.filters['severity_label'] = severity_filter

    @app.context_processor
    def inject_localization():
        current_lang = session.get('lang', 'km')
        return {
            'current_lang': current_lang,
            't': lambda key, default=None: gettext(key, lang=current_lang, default=default),
            'get_symptom_name': lambda s: get_localized_symptom(s, lang=current_lang)['name'],
            'get_symptom_desc': lambda s: get_localized_symptom(s, lang=current_lang)['description'],
            'get_disease_name': lambda d: get_localized_disease(d, lang=current_lang)['name'],
            'get_disease_desc': lambda d: get_localized_disease(d, lang=current_lang)['description'],
            'get_disease_treatment': lambda d: get_localized_disease(d, lang=current_lang)['treatment'],
            'get_disease_prevention': lambda d: get_localized_disease(d, lang=current_lang)['prevention'],
        }

    @app.route('/set-language/<lang>')
    def set_language(lang):
        if lang in ['km', 'en']:
            session['lang'] = lang
        next_url = request.referrer or url_for('diagnosis.dashboard')
        return redirect(next_url)

    register_routes(app)

    # Safely ensure database tables exist and populate sample data on startup
    with app.app_context():
        try:
            db.create_all()
            create_sample_data()
        except Exception as e:
            # Prevents app crash if DB is not yet reachable
            pass

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

        from models.seed_data import SYMPTOMS, DISEASES, RULES

        if Symptom.query.count() == 0:
            for s in SYMPTOMS:
                symptom = Symptom(**s)
                db.session.add(symptom)

        if Disease.query.count() == 0:
            for d in DISEASES:
                disease = Disease(**d)
                db.session.add(disease)

        db.session.commit()

        if DiseaseRule.query.count() == 0:
            for r in RULES:
                rule = DiseaseRule(**r)
                db.session.add(rule)

            db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Sample data creation skipped: {e}")




app = create_app()

@app.cli.command("seed-db")
def seed_db_command():
    """Seed sample data into database."""
    with app.app_context():
        create_sample_data()
        print("Database seeded successfully with users, diseases, symptoms, and rules.")

# Run locally
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )