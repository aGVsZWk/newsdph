from flask import render_template, flash, redirect, url_for, current_app, request, Blueprint
from flask_login import login_required, current_user, fresh_login_required, logout_user

from newsdph.decorators import confirm_required, permission_required
# from newsdph.emails import send_change_email_email
# from newsdph.extensions import db
# from newsdph.forms.user import EditProfileForm, UploadAvatarForm, CropAvatarForm, ChangeEmailForm, \
    # ChangePasswordForm, NotificationSettingForm, PrivacySettingForm, DeleteAccountForm
from newsdph.models import User
from newsdph.schemas import UserProfileSchema
from newsdph.utils.response import make_response

# from newsdph.notifications import push_follow_notification
# from newsdph.settings import Operations
# from newsdph.utils import generate_token, validate_token, redirect_back, flash_errors

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile/<int:id>')
def get_profile(id):
    user = User.get_user_message_by_id(id)
    schema_data = schema.dump(user)
    status = 1 if user.exist else 0
    return make_response(data=schema_data, status=status)




# @user_bp.route('/<username>')
# def index(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     if user == current_user and user.locked:
#         flash('Your account is locked.', 'danger')
#
#     if user == current_user and not user.active:
#         logout_user()
#
#     page = request.args.get('page', 1, type=int)
#     per_page = current_app.config['ALBUMY_PHOTO_PER_PAGE']
#     pagination = Photo.query.with_parent(user).order_by(Photo.timestamp.desc()).paginate(page, per_page)
#     photos = pagination.items
#     return render_template('user/index.html', user=user, pagination=pagination, photos=photos)
#
