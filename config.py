import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Flask application configuration"""
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'coffee-disease-secret-key-change-in-production'
    
    # Retrieve database URL from Vercel environment variables (checks both standard key names)
    db_url = os.environ.get('DATABASE_URL') or os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Format prefixes for SQLAlchemy driver compatibility
    if db_url:
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        elif db_url.startswith("mysql://"):
            db_url = db_url.replace("mysql://", "mysql+mysqlconnector://", 1)
        elif db_url.startswith("sqlite:///") and not db_url.startswith("sqlite:////") and not db_url.startswith("sqlite:///:memory:"):
            rel_path = db_url.replace("sqlite:///", "", 1)
            db_url = 'sqlite:///' + os.path.join(basedir, rel_path)

    # Fallback to local SQLite file for development
    SQLALCHEMY_DATABASE_URI = db_url or \
        'sqlite:///' + os.path.join(basedir, 'coffee_diseases.db')
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = False  
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'images', 'coffee_leaves')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    CASES_PER_PAGE = 20
    RULES_PER_PAGE = 20
    
    APP_NAME = 'Coffee Disease Expert System'
    APP_VERSION = '1.0.0'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    # Only enforce secure cookies if on Vercel/HTTPS or explicitly configured
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True' if os.environ.get('VERCEL') else 'False').lower() in ('true', '1')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}