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
from werkzeug.security import generate_password_hash
from flask import current_app
from flask_login import UserMixin, current_user, AnonymousUserMixin
from flask_babel import gettext
from newsdph.utils.db import fetch_to_dict, execute


def get_one_user(user_id=None, username=None, email=None, mphone=None):
    if user_id:
        q = "id=:user_id"
        params = {"user_id": user_id}
    elif username:
        q = "username=:username"
        params = {"username": username}
    elif email:
        q = "email=:email"
        params = {"email": email}
    elif mphone:
        q = "mphone=:mphone"
        params = {"mphone": mphone}
    else:
        return {}
    sql = "select a.id, a.username, a.password, a.email, a.mphone, a.confirmed, a.locked, a.actived, a.deleted, a.role_id from user as a where " + q
    user = fetch_to_dict(sql=sql, params=params, fetch="one")
    return user


def insert_one_user(updata):
    """
    插入一条数据
    :param updata:
    :return:
    """
    sql = "insert into user(username, email, mphone, password, confirmed, locked, actived, deleted, role_id) values(:username, :email, :mphone, :password, :confirmed, :locked, :actived, :deleted, :role_id)"
    execute(sql, updata)
    return True


def user_model(**kwargs):
    """
    Provide parameters, formatted as a dictionary, and then to add some other data to enter.
    提供参数，格式化为一个字典，再将其他一些数据加入进去
    :param kwargs:
    :return:
    """
    is_admin_add_user = kwargs.get("is_admin_add_user")
    unionid = kwargs.get("unionid")
    if not unionid:
        # 非第三方平台登录注册
        if not kwargs.get("username"):
            return None
        if not is_admin_add_user:
            if not kwargs.get("email") and not kwargs.get("mphone_num"):
                return None

    if not kwargs.get("role_id"):
        return None
    password = kwargs.get("password")
    if password:
        password = generate_password_hash(password)
    active = kwargs.get("active", False)
    user = {
        "username": kwargs.get("username"),
        "password": password,
        "email": kwargs.get("email"),
        'mphone': kwargs.get("mphone_num"),
        "confirmed": True,
        "locked": False,
        "actived": active,
        "deleted": False,
        "role_id": kwargs.get("role_id")
    }

    if unionid:
        platform_name = kwargs.get("platform_name", "None")
        user["login_platform"] = {platform_name: {"unionid": unionid}}
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
            self.role_id = user["role_id"]

            if not self.mphone:
                user_info_mphone_num = None
            else:
                temp_num = str(self.mphone)
                user_info_mphone_num = "{}****{}".format(
                    temp_num[0:3], temp_num[-5:-1]),
            self.user_info = {
                "username": self.username,
                "is_active": self.actived,
                "is_delete": self.deleted,
                "is_lock": self.deleted,
                "is_confirm": self.deleted,
                "email": self.email,
                "mphone": user_info_mphone_num,
                "role_id": self.role_id,
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


# @event.listens_for(User, 'before_insert')
# def add_info(mapper, connection, target):
#     info = UserInfo()
#     setting = UserSetting()
#     object_session(target).add(info)
#     object_session(target).add(setting)
#     target.info = info
#     target.setting = setting
