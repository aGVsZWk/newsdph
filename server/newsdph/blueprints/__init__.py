from newsdph.blueprints.user import user_bp
from newsdph.blueprints.resource import resource_bp

def register_blueprints(app):
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(resource_bp, url_prefix='/resource')

    # for bp in blueprints:
    #     app.register_blueprint(bp)
