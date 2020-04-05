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


# def send_mail(subject, to, html):
#     app = current_app._get_current_object()
#     message = Message(subject, recipients=[to], html=html)
#     thr = Thread(target=_send_async_mail, args=[app, message])
#     thr.start()
#     return thr
#
#
# def send_new_comment_email(post):
#     post_url = url_for('blog.show_post', post_id=post.id, _external=True) + '#comments'
#     send_mail(subject='New comment', to=current_app.config['BLUELOG_EMAIL'],
#               html='<p>New comment in post <i>%s</i>, click the link below to check:</p>'
#                    '<p><a href="%s">%s</a></P>'
#                    '<p><small style="color: #868e96">Do not reply this email.</small></p>'
#                    % (post.title, post_url, post_url))
#
#
# def send_new_reply_email(comment):
#     post_url = url_for('blog.show_post', post_id=comment.post_id, _external=True) + '#comments'
#     send_mail(subject='New reply', to=comment.email,
#               html='<p>New reply for the comment you left in post <i>%s</i>, click the link below to check: </p>'
#                    '<p><a href="%s">%s</a></p>'
#                    '<p><small style="color: #868e96">Do not reply this email.</small></p>'
#                    % (comment.post.title, post_url, post_url))


def send_mail(to, subject, template, **kwargs):
    message = Message(current_app.config['ALBUMY_MAIL_SUBJECT_PREFIX'] + subject, recipients=[to])
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr


def send_confirm_email(user, token, to=None):
    send_mail(subject='Email Confirm', to=to or user.email, template='emails/confirm', user=user, token=token)


def send_reset_password_email(user, token):
    send_mail(subject='Password Reset', to=user.email, template='emails/reset_password', user=user, token=token)


def send_change_email_email(user, token, to=None):
    send_mail(subject='Change Email Confirm', to=to or user.email, template='emails/change_email', user=user, token=token)
