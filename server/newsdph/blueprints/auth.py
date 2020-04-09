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
    username = request.json.get('username')
    password = request.json.get('password')
    remember = request.json.get('remember')
    user = User(username)
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
    status_code = 1 if status else 0
    return make_response('', status_code)


@auth_bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    code = request.json.get('code')
    print(code, redis_client.get(email))
    if not redis_client.get(email):
        return make_response('', 0)     # 验证码过期
    if code != redis_client.get(email).decode():
        return make_response('', 0)  # 验证码不存在
    User.create(email, username, password)
    return make_response('', 1)
