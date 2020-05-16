#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: response.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-10-28 19:53:26 (CST)
# Last Update: Wednesday 2018-11-21 10:31:23 (CST)
#          By:
# Description:
# **************************************************************************
from flask import make_response, jsonify, render_template


class PageInfo(object):
    def __init__(self, ins, page, number):
        self.ins = ins
        self.page = page if page > 0 else 1
        self.number = number
        self.pages = self._pages

    @property
    def _pages(self):
        if self.number == -1:
            return 1
        length = len(self.ins)
        if length % self.number == 0:
            return length // self.number
        return length // self.number + 1

    @property
    def data(self):
        if self.number == -1:
            return self.ins
        pages = self.pages
        if self.page > pages:
            self.page = pages
        return self.ins[(self.page - 1) * self.number:self.page * self.number]


class HTTPResponse(object):
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500

    def __init__(self, status_code=200, message="", data=None, pageinfo=None):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.pageinfo = pageinfo

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
            "pageinfo": self.pageinfo
        }

    def to_response(self):
        resp = dict(message=self.message)
        if self.data is not None:
            resp.update(data=self.data)
        if self.pageinfo is not None:
            resp.update(pageinfo=self.pageinfo)
        return make_response(jsonify(**resp), self.status_code)


class HTTP(object):
    @classmethod
    def OK(cls, message="ok", data=None, pageinfo=None):
        return HTTPResponse(
            HTTPResponse.OK,
            message,
            data,
            pageinfo,
        ).to_response()

    @classmethod
    def BAD_REQUEST(cls, message="bad request", data=None):
        return HTTPResponse(
            HTTPResponse.BAD_REQUEST,
            message,
            data,
        ).to_response()

    @classmethod
    def UNAUTHORIZED(cls, message="unauthorized", data=None):
        return HTTPResponse(
            HTTPResponse.UNAUTHORIZED,
            message,
            data,
        ).to_response()

    @classmethod
    def FORBIDDEN(cls, message="forbidden", data=None):
        return HTTPResponse(
            HTTPResponse.FORBIDDEN,
            message,
            data,
        ).to_response()

    @classmethod
    def NOT_FOUND(cls, message="not found", data=None):
        return HTTPResponse(
            HTTPResponse.NOT_FOUND,
            message,
            data,
        ).to_response()

    @classmethod
    def SERVER_ERROR(cls, message="internal server error", data=None):
        return HTTPResponse(
            HTTPResponse.SERVER_ERROR,
            message,
            data,
        ).to_response()

    @classmethod
    def HTML(cls, template, **kwargs):
        return render_template(template, **kwargs)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-10-28 19:52:57 (CST)
# Last Update: Thursday 2018-10-25 13:34:30 (CST)
#          By:
# Description:
# **************************************************************************
from sqlalchemy import inspect
from sqlalchemy.orm.interfaces import (ONETOMANY, MANYTOMANY)
from sqlalchemy.types import DateTime, Integer
from flask_sqlalchemy import Pagination


class Column(object):
    def __init__(self, model):
        self.inp = inspect(model)
        self.columns = self.inp.columns

    @property
    def primary_columns(self):
        return [column for column in self.columns if column.primary_key]

    @property
    def nullable_columns(self):
        return [column for column in self.columns if column.nullable]

    @property
    def notnullable_columns(self):
        return [
            column for column in self.columns
            if not column.nullable and not column.primary_key
        ]

    @property
    def unique_columns(self):
        return [column for column in self.columns if column.unique]

    @property
    def relation_columns(self):
        return [relation for relation in self.inp.relationships]

    @property
    def datetime_columns(self):
        return [
            column for column in self.columns
            if isinstance(column.type, DateTime)
        ]

    @property
    def integer_columns(self):
        return [
            column for column in self.columns
            if isinstance(column.type, Integer)
        ]

    @property
    def foreign_keys(self):
        columns = []
        [columns.extend(list(column.foreign_keys)) for column in self.columns]
        return [i.parent for i in columns]


class PageInfo(object):
    '''
    just for flask_sqlalchemy
    '''

    def __init__(self, paginate):
        self.paginate = paginate

    def as_dict(self):
        pageinfo = {
            'items': True,
            'pages': self.paginate.pages,
            'has_prev': self.paginate.has_prev,
            'page': self.paginate.page,
            'has_next': self.paginate.has_next,
            'iter_pages': list(
                self.paginate.iter_pages(
                    left_edge=1, left_current=2, right_current=3,
                    right_edge=1))
        }
        return pageinfo


class Field(object):
    def __init__(self, source, args={}, default=None):
        self.source = source
        self.args = args
        self.default = default

    def data(self, instance):
        if hasattr(instance, self.source):
            source = getattr(instance, self.source)
            if not callable(source):
                return source
            return source(**self.args)
        return self.default


class Serializer(object):
    def __init__(self, instance, **kwargs):
        meta = self.Meta
        self.instance = instance
        self.depth = kwargs['depth'] if 'depth' in kwargs else meta.depth
        self.include = kwargs[
            'include'] if 'include' in kwargs else meta.include
        self.exclude = kwargs[
            'exclude'] if 'exclude' in kwargs else meta.exclude
        self.extra = kwargs['extra'] if 'extra' in kwargs else meta.extra

    def __new__(self, *args, **kwargs):
        meta = self.Meta
        for _meta in ['include', 'exclude', 'extra']:
            if not hasattr(meta, _meta):
                setattr(meta, _meta, [])
        if not hasattr(meta, 'depth'):
            setattr(meta, 'depth', 2)
        return object.__new__(self)

    @property
    def data(self):
        if isinstance(self.instance, Pagination):
            self.instance = self.instance.items
        if isinstance(self.instance, list):
            return self._serializerlist(self.instance, self.depth)
        return self._serializer(self.instance, self.depth)

    def _serializerlist(self, instances, depth):
        results = []
        for instance in instances:
            result = self._serializer(instance, depth)
            if result:
                results.append(result)
        return results

    def _serializer(self, instance, depth):
        result = {}
        if depth == 0:
            return result
        depth -= 1
        model_class = self.get_model_class(instance)
        inp = self.get_inspect(model_class)
        model_data = self._serializer_model(inp, instance, depth)
        relation_data = self._serializer_relation(inp, instance, depth)
        extra_data = self._serializer_extra(instance)
        result.update(model_data)
        result.update(relation_data)
        result.update(extra_data)
        return result

    def _serializer_extra(self, instance):
        extra = self.extra
        result = {}
        for e in extra:
            # extra_column = getattr(self, e)
            # if isinstance(extra_column, Field):
            #     result[e] = extra_column.data(instance)
            # else:
            extra_column = getattr(instance, e)
            result[e] = extra_column if not callable(
                extra_column) else extra_column()
        return result

    def _serializer_model(self, inp, instance, depth):
        result = {}
        model_columns = self.get_model_columns(inp)
        for column in model_columns:
            result[column] = getattr(instance, column)
        return result

    def _serializer_relation(self, inp, instance, depth):
        result = {}
        relation_columns = self.get_relation_columns(inp)
        for relation in relation_columns:
            column = relation.key
            serializer = Serializer
            if hasattr(self, column):
                serializer = getattr(self, column)
            if relation.direction in [ONETOMANY, MANYTOMANY
                                      ] and relation.uselist:
                children = getattr(instance, column)
                if relation.lazy == 'dynamic':
                    children = children.all()
                result[column] = serializer(
                    children, exclude=[relation.back_populates],
                    depth=depth).data if children else []
            else:
                child = getattr(instance, column)
                if relation.lazy == 'dynamic':
                    child = child.first()
                result[column] = serializer(
                    child, exclude=[relation.back_populates],
                    depth=depth).data if child else {}
        return result

    def get_model_class(self, instance):
        return getattr(instance, '__class__')

    def get_inspect(self, model_class):
        return inspect(model_class)

    def get_model_columns(self, inp):
        if self.include:
            model_columns = [
                column.name for column in inp.columns
                if column.name in self.include
            ]
        elif self.exclude:
            model_columns = [
                column.name for column in inp.columns
                if column.name not in self.exclude
            ]
        else:
            model_columns = [column.name for column in inp.columns]

        return model_columns

    def get_relation_columns(self, inp):
        if self.include:
            relation_columns = [
                relation for relation in inp.relationships
                if relation.key in self.include
            ]
        elif self.exclude:
            relation_columns = [
                relation for relation in inp.relationships
                if relation.key not in self.exclude
            ]
        else:
            relation_columns = [relation for relation in inp.relationships]
        return relation_columns

    class Meta:
        depth = 2
        include = []
        exclude = []
        extra = []


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-12-07 14:01:14 (CST)
# Last Update: Wednesday 2018-11-21 10:49:57 (CST)
#          By:
# Description:
# **************************************************************************

from functools import wraps
from random import sample
from string import ascii_letters, digits

from flask import (flash, redirect, render_template, request, url_for, session)
from flask.views import MethodView
from flask_login import current_user, login_required
from flask_babel import gettext as _
from flask_maple.serializer import Serializer
from flask_maple.models import db
from flask_maple.response import HTTP

User = db.Model._decl_class_registry['User']


def guest_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if current_user.is_authenticated:
            flash(_("You have logined in ,needn't login again"))
            return redirect('/')
        return func(*args, **kwargs)

    return decorator


def check_params(keys):
    def _check_params(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            length = {
                'username': lambda value: 4 <= len(value) <= 20,
                'password': lambda value: 4 <= len(value) <= 20,
            }
            babel = {
                'username': _("Username"),
                'password': _("Password"),
                'email': _("Email"),
                'captcha': _("Captcha")
            }
            keys.append('captcha')
            post_data = request.json
            for key in keys:
                if not post_data.get(key):
                    msg = _('The %(key)s is required', key=babel[key])
                    return HTTP.BAD_REQUEST(message=msg)
                if not length.get(key, lambda value: True)(post_data[key]):
                    msg = _(
                        "The %(key)s's length must be between 4 to 20 characters",
                        key=babel[key])
                    return HTTP.BAD_REQUEST(message=msg)
            captcha = post_data['captcha']
            if captcha.lower() != session.pop('captcha', '00000').lower():
                msg = _('The captcha is error')
                return HTTP.BAD_REQUEST(message=msg)
            return func(*args, **kwargs)

        return decorator

    return _check_params


class LoginView(MethodView):
    decorators = [guest_required]

    def get(self):
        return render_template('auth/login.html')

    @check_params(['username', 'password'])
    def post(self):
        post_data = request.json
        username = post_data['username']
        password = post_data['password']
        remember = post_data.pop('remember', True)
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            msg = _('Username or Password Error')
            return HTTP.BAD_REQUEST(message=msg)
        user.login(remember)
        serializer = user.serializer() if hasattr(
            user, 'serializer') else Serializer(
                user, depth=1)
        return HTTP.OK(data=serializer.data)


class LogoutView(MethodView):
    decorators = [login_required]

    def get(self):
        current_user.logout()
        return redirect(request.args.get('next') or '/')


class RegisterView(MethodView):
    def get(self):
        return render_template('auth/register.html')

    @check_params(['username', 'password', 'email'])
    def post(self):
        post_data = request.json
        username = post_data['username']
        password = post_data['password']
        email = post_data['email']
        if User.query.filter_by(email=email).exists():
            msg = _('The email has been registered')
            return HTTP.BAD_REQUEST(message=msg)
        if User.query.filter_by(username=username).exists():
            msg = _('The username has been registered')
            return HTTP.BAD_REQUEST(message=msg)
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        user.login(True)
        self.send_email(user)
        flash(_('An email has been sent to your.Please receive'))
        serializer = user.serializer() if hasattr(
            user, 'serializer') else Serializer(
                user, depth=1)
        return HTTP.OK(data=serializer.data)

    def send_email(self, user):
        token = user.email_token
        confirm_url = url_for(
            'auth.confirm_token', token=token, _external=True)
        html = render_template('templet/email.html', confirm_url=confirm_url)
        subject = _("Please confirm  your email")
        user.send_email(html=html, subject=subject)


class ForgetView(MethodView):
    decorators = [guest_required]

    def get(self):
        return render_template('auth/forget.html')

    @check_params(['email'])
    def post(self):
        post_data = request.json
        email = post_data['email']
        user = User.query.filter_by(email=email).first()
        if not user:
            msg = _('The email is error')
            return HTTP.BAD_REQUEST(message=msg)
        password = ''.join(sample(ascii_letters + digits, 8))
        user.set_password(password)
        user.save()
        self.send_email(user, password)
        flash(
            _('An email has been sent to you.'
              'Please receive and update your password in time'))
        return HTTP.OK()

    def send_email(self, user, password):
        html = render_template('templet/forget.html', confirm_url=password)
        subject = "Please update your password in time"
        user.send_email(html=html, subject=subject)


class ConfirmView(MethodView):
    decorators = [login_required]

    def post(self):
        if current_user.is_confirmed:
            return HTTP.BAD_REQUEST(message=_("user has been confirmed."))
        self.send_email(current_user)
        return HTTP.OK(
            message=_('An email has been sent to your.Please receive'))

    def send_email(self, user):
        token = user.email_token
        confirm_url = url_for(
            'auth.confirm_token', token=token, _external=True)
        html = render_template('templet/email.html', confirm_url=confirm_url)
        subject = _("Please confirm  your email")
        user.send_email(html=html, subject=subject)


class ConfirmTokenView(MethodView):
    def get(self, token):
        user = User.check_email_token(token)
        if not user:
            msg = _('The confirm link has been out of time.'
                    'Please confirm your email again')
            flash(msg)
            return redirect('/')
        if user.is_confirmed:
            flash(_('The email has been confirmed. Please login.'))
            return redirect('auth.login')
        user.is_confirmed = True
        user.save()
        flash('You have confirmed your account. Thanks!')
        return redirect('/')


class Auth(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        login_view = LoginView.as_view('auth.login')
        logout_view = LogoutView.as_view('auth.logout')
        register_view = RegisterView.as_view('auth.register')
        forget_view = ForgetView.as_view('auth.forget')
        confirm_view = ConfirmView.as_view('auth.confirm')
        confirm_token_view = ConfirmTokenView.as_view('auth.confirm_token')
        app.add_url_rule('/login', view_func=login_view)
        app.add_url_rule('/logout', view_func=logout_view)
        app.add_url_rule('/register', view_func=register_view)
        app.add_url_rule('/forget', view_func=forget_view)
        app.add_url_rule('/confirm', view_func=confirm_view)
        app.add_url_rule('/confirm/<token>', view_func=confirm_token_view)
