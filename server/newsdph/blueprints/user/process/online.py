from flask import current_app
from flask_login import current_user
from newsdph.utils.verify import short_str_verifi, password_format_ver, email_format_ver, mobile_phone_format_ver
from newsdph.blueprints.user.user import get_one_user
from newsdph.utils.utils.uid import verify_capta


def p_sign_up(username, password, password2, code, email=None, mobile_phone_number=None, next=None):
    data = {}
    if current_user.is_authenticated:
        message = ("Is logged in", "s")
        error_code = 201
        data['status'] = 1
        data['to_url'] = next or current_app.config["LOGIN_IN_TO"]
        return data, error_code, message
    # 用户名格式验证
    s1, r1 = short_str_verifi(username, project="username")
    # 密码格式验证
    s2, r2 = password_format_ver(password)
    if not s1:
        message = (r1, "e")
        error_code = 422
        data['status'] = 0
    # 是否存在用户名
    elif get_one_user(username=username):
        message = ("Name has been used", "w")
        error_code = 403
        data['status'] = 0
    elif not s2:
        message = (r2, "e")
        error_code = 400
        data['status'] = 0
    # 检验两次密码
    elif password != password2:
        message = ("The two passwords don't match", e)
        error_code = 400
        data['status'] = 0
    if data:
        return data, error_code, message
    if email:
        # 邮件注册
        s, r = email_format_ver(email)
        if not s:
            message = (r, "e")
            error_code = 422
            data['status'] = 0
        elif get_one_user(email=email):
            message = ("This email has been registered in the site oh, please login directly.", "w")
            error_code = 403
            data['status'] = 0
        if data:
            return data
        # 检验验证码
        r = verify_capta(code=code, email=email)
        if not r:
            message = ("Verification code error", "e")
            error_code = 401
            return data, error_code, message

    elif mobile_phone_number:
        s, r = mobile_phone_format_ver(mobile_phone_number)
        if not s:
            message = (r, "e")
            error_code = 422
            data['status'] = 0
        elif get_one_user(mphone=mobile_phone_number):
            message = ("This number has been registered in the site oh, please login directly.", "w")
            error_code = 403
            data['status'] = 0
        if data:
            return data
        # 检验验证码
        r = verify_capta(code=code, tel_number=mobile_phone_number)
        if not r:
            message = ("Verification code error", "e")
            error_code = 401
            return data, error_code, message
    if not data:
        role_id = 1
        user = user_model(username=username,
                          email=email,
                          mphone_num=mobile_phone_number,
                          password=password,
                          role_id=role_id,
                          active=True
                            )
        r = insert_one_user(updata=user)
        if r:
            # 发送邮件

            # 发送短信
            message = ('Registered successfully', 's')
            error_code = 201
        else:
            message = ('Data saved incorrectly, please try again', 'e')
            error_code = 201
        data['to_url'] = current_app.config["LOGIN_VIEW"]
        return data, error_code, message
    return data, error_code, message