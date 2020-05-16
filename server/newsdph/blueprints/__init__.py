from newsdph.blueprints.user import user_bp

def register_blueprints(app):
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    # for bp in blueprints:
    #     app.register_blueprint(bp)
