#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-15 21:09:08 (CST)
# Last Update: Wednesday 2018-07-25 18:54:54 (CST)
#          By:
# Description:
# **************************************************************************
from datetime import datetime, timedelta

from flask import current_app
from flask_login import UserMixin, current_user, AnonymousUserMixin
from flask_babel import gettext
from newsdph.utils.db import fetch_to_dict, execute


def get_one_user(user_id=None, username=None, email=None, mphone=None):
    if user_id:
        q = "id=:user_id"
        params = {"user_id": user_id}
    elif username:
        q = "username:username"
        params = {"username": username}
    elif email:
        q = "email:email"
        params  = {"email": email}
    elif mphone:
        q = "mphone:mphone"
        params = {"mphone": mphone}
    else:
        return {}
    sql = "select a.id, a.username, a.password, a.email, a.mphone, a.confirmed, a.locked, a.actived from user as a where " + q
    user = fetch_to_dict(sql=sql, params=params, fetch="one")
    return user


class User(UserMixin):
    def __init__(self, id, **kwargs):
        super(User, self).__init__(**kwargs)
        user = get_one_user(user_id=id)
        if user:
            if "password" in user and user["password"]:
                self.no_password = False
                del user["password"]
            else:
                self.no_password = True

            self.id = id
            self.username = user["username"]
            self.email = user["email"]
            self.mphone = user["mphone"]
            self.confirmed = user["confirmed"]
            self.actived = user["actived"]
            self.locked = user["locked"]
            self.deleted = user["deleted"]

            if not self.mphone:
                user_info_mphone_num = None
            else:
                temp_num = str(self.mphone)
                user_info_mphone_num = "{}****{}".format(
                    temp_num[0:3], temp_num[-5:-1]),
            self.user_info = {
                "username": self.username,
                "is_active": self.activeed,
                "is_delete": self.deleted,
                "email": self.email,
                "mphone": user_info_mphone_num,
                # "role_id": self.role_id,
                "id": self.id
            }
        else:
            return

    @property
    def password(self):
        raise ArithmeticError(gettext('Password is not a readable attribute'))

    def validate_password(self, password):
        user = get_one_user(user_id=self.id)
        return check_password_hash(user["password"], password)

    @property
    def is_staff(self):
        return False

    @property
    def is_active(self):
        return self.actived

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def get_role_name(self):
        pass

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


@event.listens_for(User, 'before_insert')
def add_info(mapper, connection, target):
    info = UserInfo()
    setting = UserSetting()
    object_session(target).add(info)
    object_session(target).add(setting)
    target.info = info
    target.setting = setting
