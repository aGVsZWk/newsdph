from newsdph.models import User
from flask import render_template, flash, redirect, url_for, Blueprint, jsonify, request, current_app
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.extensions import db, redis_client
from newsdph.settings import Operations
from newsdph.utils.token import generate_token, validate_token
from newsdph.utils.response import make_response
from newsdph.utils.uid import get_capta
from newsdph.utils.email import send_verify_email

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')   # todo 改成form;校验工作
    password = request.json.get('password')
    remember = request.json.get('remember')
    user = User(email)
    data = {
        "id": None,
        "token": None
    }
    if user.validate_password(password) and login_user(user, remember=remember):
        data["id"] = user.data.get("id")
        data["token"] = generate_token(data["id"], operation="login").decode()

        return make_response(data, status=1)
    return make_response(data=data, status=0)


@auth_bp.route('/verify', methods=['POST'])
def verify():
    email = request.json.get('email')
    code = get_capta(length=12)
    status = redis_client.setex(email, current_app.config['VERIFY_CODE_LIFETIME'], code)
    if status:
        send_verify_email(email, code)
    return make_response('', status)


@auth_bp.route('/register', methods=['POST'])
def register():
    pass
    return render_template('expression')
