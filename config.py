import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

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

    # Fallback to local SQLite file for development
    SQLALCHEMY_DATABASE_URI = db_url or \
        'sqlite:///' + os.path.join(basedir, 'database', 'coffee_diseases.db')
        
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
    SESSION_COOKIE_SECURE = True


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