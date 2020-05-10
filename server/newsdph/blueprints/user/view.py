from flask import url_for, current_app, request, Blueprint
from flask_login import login_required, current_user, fresh_login_required, logout_user

from newsdph.decorators import confirm_required, permission_required
# from newsdph.emails import send_change_email_email
# from newsdph.extensions import db
# from newsdph.forms.user import EditProfileForm, UploadAvatarForm, CropAvatarForm, ChangeEmailForm, \
    # ChangePasswordForm, NotificationSettingForm, PrivacySettingForm, DeleteAccountForm
from newsdph.utils.response import make_response
from newsdph.utils.db import fetch_to_dict, fetch_to_dict_pagetion
from webargs.flaskparser import use_args
from . import scheme

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile/<int:id>')
# @login_required
def get_profile(id):
    sql = "select id, name, sex, hobby, age, birthday, email, username, phone, avatar, confirmed, locked, active, role_id from user where id = :id"
    params = {"id": id}
    # print(current_user)
    data = fetch_to_dict(sql=sql, params=params, fetch="one")
    status = 1 if data else 0
    return make_response(data=data, status=status)


@user_bp.route('/profile')
@login_required
@use_args(scheme.profile, location="query")
def query_profile(args):
    condition = " where id > 0"
    params = {}
    print(args)
    if args.get('name'):
        condition += " and name=:name"
        params['name'] = args.get('name')
    if args.get("sex"):
        condition += " and sex=:sex"
        params['sex'] = args.get("sex")

    if args.get("age_gte"):
        condition += " and age>=:age_gte"
        params["age_gte"] = args.get("age_gte")

    if args.get("age_lte"):
        condition += " and age<=:age_lte"
        params["age_lte"] = args.get("age_lte")

    if args.get("birday_gte"):
        condition += " and birthday>=:birday_gte"
        params["birday_gte"] = args.get("birday_gte")

    if args.get("birday_lte"):
        condition += " and birthday<=:birday_lte"
        params["birday_lte"] = args.get("birday_lte")

    if args.get("email"):
        condition += " and email=:email"
        params["email"] = args.get("email")

    page = args.get('page')
    size = args.get("page_size")
    sql = "select id, name, sex, hobby, age, birthday, email, username, phone, avatar, confirmed, locked, active, role_id from user" + condition
    if page and size:
        data = fetch_to_dict_pagetion(sql=sql, params=params, page=page, page_size=size)
    else:
        data = fetch_to_dict_pagetion(sql=sql, params=params,)
    status = 1 if data else 0
    print(data)
    return make_response(data=data, status=status)
