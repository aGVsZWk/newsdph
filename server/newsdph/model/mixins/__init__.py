from .db import UserMixin as _UserMixin
from .mail import MailMixin
from .model import ModelMixin

class UserMixin(_UserMixin, MailMixin, ModelMixin):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def username(cls):
        return db.Column(db.String(512), nullable=False, unique=True)

    @declared_attr
    def email(cls):
        return db.Column(db.String(512), nullable=False, unique=True)

    @declared_attr
    def password(cls):
        return db.Column(db.String(512), nullable=False)

    @declared_attr
    def is_superuser(cls):
        return db.Column(db.Boolean, default=False)

    @declared_attr
    def is_confirmed(cls):
        return db.Column(db.Boolean, default=False)

    @declared_attr
    def register_time(cls):
        return db.Column(db.DateTime, default=datetime.now)

    @declared_attr
    def last_login(cls):
        return db.Column(db.DateTime, default=datetime.now)

    @declared_attr
    def groups(cls):
        return db.relationship(
            'Group',
            secondary=user_group,
            backref=db.backref('users', lazy='dynamic'),
            lazy='dynamic')

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)
        return self.password

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    @property
    def is_logined(self):
        return self.is_authenticated

    def login(self, remember=True):
        login_user(self, remember)

    def logout(self):
        logout_user()

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<User %r>' % self.username
