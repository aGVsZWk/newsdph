# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from threading import Thread

from flask import url_for, current_app, render_template
from flask_mail import Message

from newsdph.extensions import mail


def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)


def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject, recipients=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr


def send_new_comment_email(post):
    post_url = url_for('blog.show_post', post_id=post.id, _external=True) + '#comments'
    send_mail(subject='New comment', to=current_app.config['BLUELOG_EMAIL'],
              html='<p>New comment in post <i>%s</i>, click the link below to check:</p>'
                   '<p><a href="%s">%s</a></P>'
                   '<p><small style="color: #868e96">Do not reply this email.</small></p>'
                   % (post.title, post_url, post_url))


def send_new_reply_email(comment):
    post_url = url_for('blog.show_post', post_id=comment.post_id, _external=True) + '#comments'
    send_mail(subject='New reply', to=comment.email,
              html='<p>New reply for the comment you left in post <i>%s</i>, click the link below to check: </p>'
                   '<p><a href="%s">%s</a></p>'
                   '<p><small style="color: #868e96">Do not reply this email.</small></p>'
                   % (comment.post.title, post_url, post_url))

def send_verify_email(email, code):
    send_mail(subject='New register', to=email,
              html='<p>Your register code is %s </p>' % code)



# def send_mail(to, subject, template, **kwargs):
#     message = Message(current_app.config['ALBUMY_MAIL_SUBJECT_PREFIX'] + subject, recipients=[to])
#     message.body = render_template(template + '.txt', **kwargs)
#     message.html = render_template(template + '.html', **kwargs)
#     app = current_app._get_current_object()
#     thr = Thread(target=_send_async_mail, args=[app, message])
#     thr.start()
#     return thr
#
#
# def send_confirm_email(user, token, to=None):
#     send_mail(subject='Email Confirm', to=to or user.email, template='emails/confirm', user=user, token=token)
#
#
# def send_reset_password_email(user, token):
#     send_mail(subject='Password Reset', to=user.email, template='emails/reset_password', user=user, token=token)
#
#
# def send_change_email_email(user, token, to=None):
#     send_mail(subject='Change Email Confirm', to=to or user.email, template='emails/change_email', user=user, token=token)


#
# #!/usr/bin/env python
# # -*- coding=UTF-8 -*-
# # *************************************************************************
# #   Copyright © 2015 JiangLin. All rights reserved.
# #   File Name: mail.py
# #   Author:JiangLin
# #   Mail:mail@honmaple.com
# #   Created Time: 2015-11-27 21:59:02
# # *************************************************************************
# from flask_mail import Mail as _Mail
# from flask_mail import Message
# from threading import Thread
# from itsdangerous import (URLSafeTimedSerializer, BadSignature,
#                           SignatureExpired)
# from flask import current_app
# from .utils import gen_secret_key
#
# mail = _Mail()
#
#
# class Mail(object):
#     def __init__(self, app=None):
#         if app is not None:
#             self.init_app(app)
#
#     def init_app(self, app):
#         self.app = app
#         mail.init_app(app)
#
#     def send_async_email(self, msg):
#         with self.app.app_context():
#             mail.send(msg)
#
#     def send_email(self, *args, **kwargs):
#         msg = Message(*args, **kwargs)
#         thr = Thread(target=self.send_async_email, args=[msg])
#         thr.start()
#
#
# class MailMixin(object):
#     @classmethod
#     def _token_serializer(cls, key=None, salt=None):
#         config = current_app.config
#         if key is None:
#             key = config.setdefault('SECRET_KEY', gen_secret_key(24))
#         if salt is None:
#             salt = config.setdefault('SECRET_KEY_SALT', gen_secret_key(24))
#         return URLSafeTimedSerializer(key, salt=salt)
#
#     @property
#     def email_token(self):
#         serializer = self._token_serializer()
#         token = serializer.dumps(self.email)
#         return token
#
#     @classmethod
#     def check_email_token(cls, token, max_age=259200):
#         serializer = cls._token_serializer()
#         try:
#             email = serializer.loads(token, max_age=max_age)
#         except BadSignature:
#             return False
#         except SignatureExpired:
#             return False
#         user = cls.query.filter_by(email=email).first()
#         if user is None:
#             return False
#         return user
#
#     # def send_email(self, *args, **kwargs):
#     #     kwargs.update(recipients=[self.email])
#     #     mail.send_email(*args, **kwargs)
#
#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # **************************************************************************
# # Copyright © 2016 jianglin
# # File Name: utils.py
# # Author: jianglin
# # Email: mail@honmaple.com
# # Created: 2016-12-07 13:16:28 (CST)
# # Last Update: Wednesday 2018-11-21 10:44:41 (CST)
# #          By:
# # Description:
# # **************************************************************************
# import os
# from sqlalchemy import inspect
#
#
# def gen_secret_key(length):
#     return os.urandom(length)
#
#
# def get_model_columns(model_class):
#     inp = inspect(model_class)
#     return [column.name for column in inp.columns]
#
#
# def get_relation_columns(model_class):
#     inp = inspect(model_class)
#     c = []
#     for relation in inp.relationships:
#         relation_inp = inspect(relation.mapper.class_)
#         for column in relation_inp.columns:
#             key = relation.key + '__' + column.name
#             c.append(key)
#     return c
#
#
# def get_columns(model_class):
#     model_columns = get_model_columns(model_class)
#     relation_columns = get_relation_columns(model_class)
#     model_columns.extend(relation_columns)
#     return model_columns
