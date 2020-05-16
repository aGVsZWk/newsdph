# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time : 2017/11/1 ~ 2019/9/1
# @Author : Allen Woo
from flask import url_for
from flask_login import current_user
import regex as re

def short_str_verifi(short_str, project=None, allow_special_chart=False):
    """
    各种名字短字符串验证
    Character name to verify
    :param s:
    allow_special_chart: 是否允许特殊字符
    :return:
    """
    if True:
        return True, ""
    else:
        return False, "short str verifi error"


def password_format_ver(password):
    """
    密码格式检验
    :param password:
    :return:
    """
    if len(password) < 8:
        return False, 'Password at least 8 characters! And at least contain Numbers, letters, special characters of two kinds'
    else:
        too_simple = True
        last_ac = False
        for p in password:
            _ac = ord(p)
            if last_ac:
                if _ac != last_ac + 1:
                    too_simple = False
                    break
            last_ac = _ac
        if too_simple:
            return False, 'The password is too simple, can not use continuous characters!'
    return True, ""

def email_format_ver(email):
    """
    邮箱字符验证
    Character email to verify
    :param email:
    :return:
    """

    if re.search(
        r"^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",
            email):
        return True, ""
    else:
        return False, "The email format is not correct"


def mobile_phone_format_ver(number):
    """
    手机号字符验证
    Character mobile phone to verify
    :param email:
    :return:
    """

    if re.search(r"^[0-9]{11}$", number):
        return True, ""
    else:
        return False, "The email format is not correct"


# def ver_user_domainhacks(domain):
#     """
#     用户个性域名验证
#     Character name to verify
#     :param name:
#     :return:
#     """
#     s, r = arg_verify(
#         reqargs=[
#             (gettext("custom domain"), domain)], required=True)
#     if not s:
#         return False, r["msg"]
#     if not re.search(r"[0-9a-zA-Z]{4}", domain):
#         return False, gettext(
#             "The domain format is not correct,Only use Numbers, letters, and at least 4 characters")
#     else:
#         return True, gettext("")
#
#
# def email_format_ver(email):
#     """
#     邮箱字符验证
#     Character email to verify
#     :param email:
#     :return:
#     """
#
#     if re.search(
#         r"^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",
#             email):
#         return True, ""
#     else:
#         return False, gettext("The email format is not correct")
#
#
# def mobile_phone_format_ver(number):
#     """
#     邮箱字符验证
#     Character email to verify
#     :param email:
#     :return:
#     """
#
#     if re.search(r"^[0-9]{11}$", number):
#         return True, ""
#     else:
#         return False, gettext("The email format is not correct")
#
#
# def url_format_ver(url):
#
#     if re.search(
#         r"(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?",
#             url):
#         return True, ""
#     else:
#         return False, gettext("The url format is not correct")
#
#
# def password_format_ver(password):
#     """
#     密码格式检验
#     :param password:
#     :return:
#     """
#
#     if len(password) < 8:
#         return False, gettext(
#             'Password at least 8 characters! And at least contain Numbers, letters, special characters of two kinds')
#     else:
#         too_simple = True
#         last_ac = False
#         for p in password:
#             _ac = ord(p)
#             if last_ac:
#                 if _ac != last_ac + 1:
#                     too_simple = False
#                     break
#             last_ac = _ac
#         if too_simple:
#             return False, gettext(
#                 'The password is too simple, can not use continuous characters!')
#     return True, ""
#
#
# def content_attack_defense(content):
#     """
#     外站链接过滤
#     :param content:
#     :return:
#     """
#     switch = get_config("security", "SWITCH")
#     security = 100
#     if switch:
#         wlists = get_config("security", "LINK_WHITELIST")
#         r = re.findall(r".*(http[s]?://[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.?[a-zA-Z0-9-]{0,10})",
#                      content)
#         if r:
#             for link in r:
#                 if link not in wlists:
#                     new_link = url_for('theme_view.link_unaudited', url=link)
#                     # new_link = link.replace(".", ". ").replace("/", "/ ").replace("&", "&amp;").replace("?", "&;")
#                     # new_link = "{}[{}]".format(new_link, gettext("Unvalidated link"))
#                     content = content.replace(link, new_link)
#                     security -= 5
#
#         temp_content = content
#         rules = mdbs["sys"].db.audit_rules.find({"project": "content_security"})
#         for rule in rules:
#             content = re.sub(r".*{}".format(rule["rule"]), "[Illegal content]", content)
#         if temp_content != content:
#             security -= 20
#             content = content.replace("<", "&lt").replace(">", "&gt")
#     return {"content": content, "security": security}
#


#
# try:
#     from urlparse import urlparse, urljoin
# except ImportError:
#     from urllib.parse import urlparse, urljoin
# from flask import request, redirect, url_for, current_app, flash
# import os
# import uuid
# import PIL
# from PIL import Image
# from itsdangerous import BadSignature, SignatureExpired
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from newsdph.settings import Operations
#
#
#
# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
#
#
# def redirect_back(default='blog.index', **kwargs):
#     for target in request.args.get('next'), request.referrer:
#         if not target:
#             continue
#         if is_safe_url(target):
#             return redirect(target)
#     return redirect(url_for(default, **kwargs))
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in current_app.config['BLUELOG_ALLOWED_IMAGE_EXTENSIONS']
#
#
# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and \
#            ref_url.netloc == test_url.netloc
#
#
#
# def flash_errors(form):
#     for field, errors in form.errors.items():
#         for error in errors:
#             flash(u"Error in the %s field - %s" % (
#                 getattr(form, field).label.text,
#                 error
#             ))
