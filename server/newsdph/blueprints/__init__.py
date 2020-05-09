# from newsdph.blueprints.admin import admin_bp
from .auth import auth_bp
from .user.view import user_bp
# from newsdph.blueprints.main import main_bp


def register_blueprints(app):
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')

    # for bp in blueprints:
    #     app.register_blueprint(bp)
