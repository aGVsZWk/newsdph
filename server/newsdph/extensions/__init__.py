#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-02-11 14:52:12 (CST)
# Last Update: Saturday 2018-03-03 21:53:59 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
# from flask_migrate import Migrate
from flask_avatars import Avatars
# from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_mail import Mail
from flask_moment import Moment
from flask_whooshee import Whooshee
from flask_socketio import SocketIO
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_marshmallow import Marshmallow
from . import babel, login


# from flask import request
# from flask_avatar import Avatar
# from flask_principal import Principal
# from flask_msearch import Search
# from flask_caching import Cache

db = SQLAlchemy()
csrf = CSRFProtect()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
toolbar = DebugToolbarExtension()
# migrate = Migrate()
dropzone = Dropzone()
whooshee = Whooshee()
avatars = Avatars()
socketio = SocketIO()
oauth = OAuth()
cors = CORS()
redis_client = FlaskRedis()
ma = Marshmallow()

# cache = Cache()
mail = Mail()
# principal = Principal()
# search = Search(db=db)
# avatar = Avatar(cache=cache.cached(
#     timeout=259200, key_prefix=lambda: "avatar:{}".format(request.url)))


def register_extensions(app):
    db.init_app(app)
    # csrf.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # toolbar.init_app(app)
    dropzone.init_app(app)
    whooshee.init_app(app)
    avatars.init_app(app)
    # socketio.init_app(app)
    oauth.init_app(app)
    cors.init_app(app)
    redis_client.init_app(app)
    # migrate.init_app(app, db)
    babel.init_app(app)
    # cache.init_app(app)
    # avatar.init_app(app)
    # principal.init_app(app)
    # search.init_app(app)
    login.init_app(app)
