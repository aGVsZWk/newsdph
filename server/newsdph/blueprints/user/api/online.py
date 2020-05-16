from flask import Blueprint, jsonify, request, current_app
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.settings import Operations
from newsdph.utils.token import generate_token
from newsdph.utils.response import make_response
from newsdph.utils.uid import get_capta
from newsdph.utils.db import fetch_to_dict
from newsdph.schemas import AuthLoginSchema, AuthVerifySchema, AuthRegisterSchema
from werkzeug.security import check_password_hash
from newsdph.blueprints.user import user_bp
from newsdph.blueprints.user.process.online import p_sign_up

# 注册
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    password2 = data.get('password2')
    code = data.get('code')
    mphone = data.get('mphone')
    data, error_code, message = p_sign_up(username=username,
                                          password=password,
                                          password2=password,
                                          code=code,
                                          email=email,
                                          mobile_phone_number=mphone)
    return make_response(data, error_code, message)



# 登录
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    schema = AuthLoginSchema()
    validated_data = schema.load(data)
    user_data = fetch_to_dict(sql, params, fetch="one")

    if user.exist and check_password_hash(user.password_hash, validated_data['password']) and login_user(user, remember=validated_data['remember']):
        schema_data = schema.dump(user)
        schema_data["token"] = generate_token(schema_data["id"], operation="login").decode()
        return make_response(schema_data, status=1)
    return make_response(data=schema_data, status=0)



# 获取验证码
@user_bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    schema = AuthVerifySchema()
    validated_data = schema.load(data)
    email = validated_data["email"]
    code = get_capta(length=12)
    # status = redis_client.setex(email, current_app.config['VERIFY_CODE_LIFETIME'], code)
    if status:
        send_verify_email(email, code)
    status_code = 1 if status else 0
    return make_response('', status_code)
