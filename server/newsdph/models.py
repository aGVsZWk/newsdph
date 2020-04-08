import hashlib
from datetime import datetime

from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from newsdph.extensions import login_manager, db
from newsdph.utils.db import execute, fetch_to_dict


class User(UserMixin):

    def __init__(self, email, **kwargs):
        sql = "select id, email,username, password, phone, avatar, confirmed, locked, active, role_id from user where email=:email"
        params = {"email": email}
        data = fetch_to_dict(sql=sql, params=params, fecth="one")
        self.id = data['id']
        self.email = data['email']
        self.username = data['username']
        self.password_hash = data['password']
        self.phone = data['phone']
        self.avatar = data['avatar']
        self.confirmed = data['confirmed']
        self.locked = data['locked']
        self.active = data['active']
        self.role_id = data['role_id']
        self.data= data
        super(User, self).__init__(**kwargs)
        # self.generate_email_hash()


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        sql = "update user set password = :password where id= :id"
        params = {"password":self.password_hash, "id":self.id}
        execute(sql, params)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_email_hash(self):
        if self.email is not None and self.email_hash is None:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()  # encode for py23 compatible

    @property
    def is_admin(self):
        return self.email == current_app.config['NEWSDPH_ADMIN_EMAIL']

    @property
    def gravatar(self):
        return 'https://gravatar.com/avatar/%s?d=monsterid' % self.email_hash
