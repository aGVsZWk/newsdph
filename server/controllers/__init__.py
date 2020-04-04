# -*- coding: utf-8 -*-

from server.controllers import news, users

blueprints = [
    news.news_bp,
    users.users_bp
]
