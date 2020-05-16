from flask import Blueprint, jsonify, request, current_app
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.settings import Operations
from newsdph.utils.token import generate_token
from newsdph.utils.response import make_response
from newsdph.utils.uid import get_capta
from newsdph.utils.db import fetch_to_dict
from newsdph.schemas import AuthLoginSchema, AuthVerifySchema, AuthRegisterSchema
from newsdph.blueprints.user import user_bp
from newsdph.blueprints.user.process.online import p_sign_up, p_sign_in

# 注册
@user_bp.route('/register', methods=['POST'])
def register():
    """
    POST:
        1.普通用户使用邮箱注册a
        emial:<emial>, 邮箱
        username: <str>, 用户名
        password: <str>,密码
        password2: <str>,再次确认密码
        code:<str>, 邮箱收取到的code


        2.普通用户使用手机注册a
        mobile_phone_number:<int>手机号码
        username: <str>, 用户名
        password: <str>,密码
        password2: <str>,再次确认密码
        code:<str>, 手机收取到的code

        :return:
    """
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    password2 = data.get('password2')
    code = data.get('code')
    mphone = data.get('mphone')
    if not email and not mphone:
        return make_response(data={}, code=400, message=("参数不全", "e"))
    print(email, username, password, password2, code, mphone)
    data, error_code, message = p_sign_up(username=username,
                                          password=password,
                                          password2=password2,
                                          code=code,
                                          email=email,
                                          mobile_phone_number=mphone)
    return make_response(data, error_code, message)


@user_bp.route('/re-authenticate', methods=['GET', 'POST'])
@login_required
def re_authenticate():
    if login_fresh():
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit() and current_user.validate_password(form.password.data):
        confirm_login()
        return redirect_back()
    return render_template('auth/login.html', form=form)


# 登录
@user_bp.route('/login', methods=['POST'])
def login():
    """
    PUT:
        1.普通登录
        username: <str>, 用户名或邮箱或手机号码
        password: <str>,密码
        remember_me:<bool>,是否保存密码
        next:<str>, 登录后要返回的to url, 如果为空,则返回设置中的LOGIN_TO
        use_jwt_auth:<int>, 是否使用jwt验证. 0 或 1,默认为0不使用

        当多次输入错误密码时，api会返回open_img_verif_code:true,
        表示需要图片验证码验证,客户端应该请求验证码/api/vercode/image,
         然后后再次提交登录时带下如下参数
        再次提交登录时需要以下两个参数
        code:<str>, 图片验证码中的字符
        code_url_obj:<json>,图片验证码url 对象
        :return:

        2.第三方登录
        待开发插件入口
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    code = data.get("code", "").strip()
    code_url = data.get("code_url", "").strip()
    remember_me = data.get("remember_me")
    use_jwt_auth = data.get("use_jwt_auth", 0)
    data, error_code, message = p_sign_in(
        username=username,
        password=password,
        password2=password2,
        code=code, code_url=code_url,
        remember_me=remember_me,
        use_jwt_auth=use_jwt_auth)
    return make_response(data, error_code, messages)




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
