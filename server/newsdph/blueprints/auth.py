from newsdph.models import User
from flask import Blueprint, jsonify, request, current_app
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.extensions import redis_client
from newsdph.settings import Operations
from newsdph.utils.token import generate_token, validate_token
from newsdph.utils.response import make_response
from newsdph.utils.uid import get_capta
from newsdph.utils.email import send_verify_email
from newsdph.utils.db import fetch_to_dict
from newsdph.schemas import AuthLoginSchema, AuthVerifySchema, AuthRegisterSchema
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

from sql import *
from sql.aggregate import *
from sql.conditionals import *


# 登录
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    schema = AuthLoginSchema()
    validated_data = schema.load(data)
    user = Table('user')
    select = user.select(user.id, user.password, user.register_time, user.last_login_time, user.avatar, user.confirmed, user.locked, user.actived)
    select.where = user.username == validated_data['username']
    sql, params = tuple(select)
    user_data = fetch_to_dict(sql, params, fetch="one")
    print(user_data)


    if user.exist and check_password_hash(user.password_hash, validated_data['password']) and login_user(user, remember=validated_data['remember']):
        schema_data = schema.dump(user)
        schema_data["token"] = generate_token(schema_data["id"], operation="login").decode()
        return make_response(schema_data, status=1)
    return make_response(data=schema_data, status=0)

# 获取验证码
@auth_bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    schema = AuthVerifySchema()
    validated_data = schema.load(data)
    email = validated_data["email"]
    code = get_capta(length=12)
    status = redis_client.setex(email, current_app.config['VERIFY_CODE_LIFETIME'], code)
    if status:
        send_verify_email(email, code)
    status_code = 1 if status else 0
    return make_response('', status_code)

# 注册
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    schema = AuthRegisterSchema()
    validated_data = schema.load(data)
    email = validated_data.get('email')
    username = validated_data.get('username')
    password = validated_data.get('password')
    code = validated_data.get('code')
    store_code = redis_client.get(email)
    if not store_code:
        return make_response('', 0)     # 验证码过期
    if code != store_code.decode():
        return make_response('', 0)  # 验证码不存在
    User.create(email, username, password)
    return make_response('', 1)
