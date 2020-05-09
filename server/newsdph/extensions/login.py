from flask_login import LoginManager, AnonymousUserMixin

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from newsdph.models import User
    user = User(user_id)
    return user


class Guest(AnonymousUserMixin):

    def can(self, permission_name):
        return False

    @property
    def is_admin(self):
        return False

def init_app(app):
    login_manager.login_message = 'Your custom message'
    login_manager.login_message_category = 'warning'

    login_manager.refresh_view = 'auth.re_authenticate'
    # login_manager.needs_refresh_message = 'Your custom message'
    login_manager.needs_refresh_message_category = 'warning'

    login_manager.anonymous_user = Guest


    login_manager.login_view = "auth.login"
    # remember me only work with `basic` rathar than `strong`
    login_manager.session_protection = "basic"
    # login_manager.login_message = _("Please login to access this page.")
    # login_manager.anonymous_user = Anonymous
    login_manager.init_app(app)
