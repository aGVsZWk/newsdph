# -*- coding: utf-8 -*-

from flask import Flask
from server import configs
from server.controllers import blueprints
from flask_cors import CORS
from server.extensions import db
__all__ = ['create_app']
DEFAULT_APP_NAME = 'NewsHub'


def create_app(app_name=None, config=None):
    if app_name is None:
        app_name = DEFAULT_APP_NAME

    app = Flask(app_name)
    configure_app(app, config)
    register_extensions(app)
    return app

def register_extensions(app):
    CORS(app)
    db.init_app(app)


def configure_app(app, config):
    app.config.from_object(configs.BaseConfig())

    if not config:
        config = configs.config_map['dev']

    app.config.from_object(config)

    # register blueprints
    for bp in blueprints:
        app.register_blueprint(bp)
