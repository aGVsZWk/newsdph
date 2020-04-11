
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
# from flask_migrate import Migrate
from flask_avatars import Avatars
# from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_whooshee import Whooshee
from flask_socketio import SocketIO
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
toolbar = DebugToolbarExtension()
# migrate = Migrate()
dropzone = Dropzone()
whooshee = Whooshee()
avatars = Avatars()
socketio = SocketIO()
oauth = OAuth()
cors = CORS()
redis_client = FlaskRedis()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    from newsdph.models import User
    user = User(user_id)
    return user


login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'

login_manager.refresh_view = 'auth.re_authenticate'
# login_manager.needs_refresh_message = 'Your custom message'
login_manager.needs_refresh_message_category = 'warning'


class Guest(AnonymousUserMixin):

    def can(self, permission_name):
        return False

    @property
    def is_admin(self):
        return False


login_manager.anonymous_user = Guest
