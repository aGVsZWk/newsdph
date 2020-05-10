import hashlib
from datetime import datetime

from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from newsdph.extensions import db
from newsdph.extensions.login import login_manager
from newsdph.utils.db import execute, fetch_to_dict


class User(UserMixin):
    @classmethod
    def get_user_message_by_id(cls, id, *args, **kwargs):
        sql = "select id, name, sex, hobby, age, birthday, email, address, phone, avatar, role_id, locked from user where id=:id"
        params = {"id": id}
        data = fetch_to_dict(sql=sql, params=params, fetch="one")
        cls.exist = True if data else False
        cls.id = data['id']
        cls.name = data['name']
        cls.sex = data['sex']
        cls.hobby = data['hobby']
        cls.age = data['age']
        cls.birthday = data['birthday']
        cls.email = data['email']
        cls.address = data['address']
        cls.phone = data['phone']
        cls.avatar = data['avatar']
        cls.locked = data['locked']
        cls.role_id = data['role_id']
        return super().__new__(cls, *args, **kwargs)

    def get_roles(self):
        sql = ""
        role = ["admin", "user", ['moderator', 'contributor']]

    @classmethod
    def query_user(cls, **kwargs):
        basesql = 'select id, name, sex, age, birthday, email, username,' + \
            ' address, phone, register_time, login_time, confirmed, locked,' + \
            ' active, role_id from user where id > 0 '
        condition = ''
        if kwargs.get('name'):
            condition += 'and name = :name'
        if kwargs.get('sex'):
            condition += 'and sex = :sex'

        # name, sex, age, age_gt, age_lt, age_gte, age_lte, birday,
        # birday_gt, birday_lt, birday_gte, birday_lte, email, username, address,
        # phone, register_time_gt, register_time_lt, register_time_gte,
        # register_time_lte, login_time_gt, login_time_lt, login_time_gte,
        # login_time_lte, confirmed, locked, active, role, order, desc

        pass

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        sql = "update user set password = :password where id= :id"
        params = {"password": self.password_hash, "id": self.id}
        execute(sql, params)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_email_hash(self):
        if self.email is not None and self.email_hash is None:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()  # encode for py23 compatible

    @classmethod
    def get_user_by_username(cls, username, *args, **kwargs):
        sql = "select id, confirmed, password, locked, active from user where username=:username"
        params = {"username": username}
        data = fetch_to_dict(sql=sql, params=params, fetch="one")
        cls.exist = True if data else False
        cls.id = data.get("id")
        cls.confirmed = data.get('confirmed')
        cls.locked = data.get('locked')
        cls.active = data.get('active')
        cls.password_hash = data.get('password')
        return super().__new__(cls, *args, **kwargs)

    @property
    def is_admin(self):
        return self.email == current_app.config['NEWSDPH_ADMIN_EMAIL']

    @property
    def gravatar(self):
        return 'https://gravatar.com/avatar/%s?d=monsterid' % self.email_hash

    @staticmethod
    def create(email, username, password):
        password_hash = generate_password_hash(password)
        params = {
            "email": email,
            "username": username,
            "password_hash": password_hash
        }
        sql = "insert into user (email, username, password) values (:email, :username, :password_hash)"
        execute(sql, params)
