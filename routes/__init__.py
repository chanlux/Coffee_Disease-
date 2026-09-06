def register_routes(app):
    from routes.auth import auth_bp
    from routes.diagnosis import diagnosis_bp
    from routes.rules import rules_bp
    from routes.cases import cases_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(diagnosis_bp)
    app.register_blueprint(rules_bp)
    app.register_blueprint(cases_bp)