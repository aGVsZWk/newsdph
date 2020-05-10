from sqlalchemy.ext.declarative import declared_attr
from .extensions import db
from datetime import datetime


class ModelMixin(object):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)


class ModelTimeMixin(ModelMixin):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, default=datetime.now)

    @declared_attr
    def updated_at(cls):
        return db.Column(
            db.DateTime, default=datetime.now, onupdate=datetime.now)


class ModelUserMixin(ModelTimeMixin):
    @declared_attr
    def user_id(cls):
        return db.Column(
            db.Integer,
            db.ForeignKey('user.id', ondelete="CASCADE"),
            nullable=False)

    @declared_attr
    def user(cls):
        name = cls.__name__.lower()
        if not name.endswith('s'):
            name = name + 's'
        if hasattr(cls, 'user_related_name'):
            name = cls.user_related_name
        return db.relationship(
            'User',
            backref=db.backref(name, cascade='all,delete', lazy='dynamic'),
            uselist=False,
            lazy='joined')


class MailMixin(object):
    @classmethod
    def _token_serializer(cls, key=None, salt=None):
        config = current_app.config
        if key is None:
            key = config.setdefault('SECRET_KEY', gen_secret_key(24))
        if salt is None:
            salt = config.setdefault('SECRET_KEY_SALT', gen_secret_key(24))
        return URLSafeTimedSerializer(key, salt=salt)

    @property
    def email_token(self):
        serializer = self._token_serializer()
        token = serializer.dumps(self.email)
        return token

    @classmethod
    def check_email_token(cls, token, max_age=259200):
        serializer = cls._token_serializer()
        try:
            email = serializer.loads(token, max_age=max_age)
        except BadSignature:
            return False
        except SignatureExpired:
            return False
        user = cls.query.filter_by(email=email).first()
        if user is None:
            return False
        return user




class UserMixin(object):
    '''
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    '''

    if not PY2:  # pragma: no cover
        # Python 3 implicitly set __hash__ to None if we override __eq__
        # We set it back to its default implementation
        __hash__ = object.__hash__

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return text_type(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class AnonymousUserMixin(object):
    '''
    This is the default object for representing an anonymous user.
    '''
    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return



class GroupMixin(ModelMixin):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def name(cls):
        return db.Column(db.String(512), nullable=False, unique=True)

    @declared_attr
    def parent_id(cls):
        return db.Column(db.Integer, db.ForeignKey('group.id'))

    @declared_attr
    def parent_group(cls):
        return db.relationship(
            'Group',
            remote_side=[cls.id],
            backref=db.backref(
                'child_groups', remote_side=[cls.parent_id], lazy='dynamic'),
            lazy='joined',
            uselist=False)

    def get_child_groups(self, depth=1):
        child_groups = self.child_groups.all()
        depth -= 1
        if depth > 0:
            child_groups.extend([
                g for group in child_groups
                for g in group.get_child_groups(depth)
            ])
        return list(set(child_groups))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Group %r>' % self.name


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

class Permission(db.Model, PermissionMixin):
    __tablename__ = 'permission'


class Group(db.Model, GroupMixin):
    __tablename__ = 'group'


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    followers = db.relationship(
        'User',
        secondary=user_follower,
        primaryjoin=(id == user_follower.c.user_id),
        secondaryjoin=(id == user_follower.c.follower_id),
        backref=db.backref(
            'following_users', lazy='dynamic'),
        lazy='dynamic')

    def is_followed(self, user=None):
        if user is None:
            user = current_user
        return db.session.query(user_follower).filter(
            user_follower.c.user_id == self.id,
            user_follower.c.follower_id == user.id).exists()

    def login(self, remember=True):
        login_user(self, remember)
        identity_changed.send(
            current_app._get_current_object(), identity=Identity(self.id))

    def logout(self):
        logout_user()
        identity_changed.send(
            current_app._get_current_object(), identity=AnonymousIdentity())

    @property
    def is_not_confirmed(self):
        return (not self.is_confirmed and self.id == current_user.id)

    @property
    def is_online(self):
        setting = self.setting
        if setting.online_status == UserSetting.STATUS_ALLOW_ALL:
            return self.username in load_online_sign_users()
        elif setting.online_status == UserSetting.STATUS_ALLOW_AUTHENTICATED:
            return self.username in load_online_sign_users(
            ) and current_user.is_authenticated
        elif setting.online_status == UserSetting.STATUS_ALLOW_OWN:
            return current_user.id == self.id
        return False

    @property
    def topic_count(self):
        return self.topics.count()

    @topic_count.setter
    def topic_count(self, value):
        return Count.user_topic_count(self.id, value)

    @property
    def reply_count(self):
        return self.replies.count()

    @reply_count.setter
    def reply_count(self, value):
        return Count.user_reply_count(self.id, value)

    @property
    def message_count(self):
        # return self.receive_messages.filter_by(status='0').count()
        return Count.user_message_count(self.id)

    @message_count.setter
    def message_count(self, value):
        return Count.user_message_count(self.id, value)

    @property
    def send_email_time(self):
        # return self.receive_messages.filter_by(status='0').count()
        return Count.user_email_time(self.id)

    @send_email_time.setter
    def send_email_time(self, value):
        return Count.user_email_time(self.id, value)

    @property
    def email_is_allowed(self):
        t = self.send_email_time
        t = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        if t + timedelta(hours=3) < now:
            self.send_email_time = now.strftime('%Y-%m-%d %H:%M:%S')
            return True
        return False

    def send_email(self, *args, **kwargs):
        kwargs.update(recipients=[self.email])
        mail.send_email(*args, **kwargs)

    def send_email_to_admin(self):
        ''''
        When someone registered an account,send email to admin.
        '''
        recipients = current_app.config['RECEIVER']
        subject = '{} has registered an account.'.format(self.username)
        html = '<p>username: {}</p><p>email: {}</p>'.format(self.username,
                                                            self.email)
        mail.send_email(subject=subject, html=html, recipients=recipients)


class UserInfo(db.Model, ModelMixin):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(128))
    school = db.Column(db.String(128), nullable=True)
    word = db.Column(db.Text, nullable=True)
    introduce = db.Column(db.Text, nullable=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey(
            'user.id', ondelete="CASCADE"))
    user = db.relationship(
        User,
        backref=db.backref(
            "info", uselist=False, cascade='all,delete', lazy='joined'),
        uselist=False,
        lazy='joined')

    def __repr__(self):
        return "<UserInfo %r>" % str(self.id)

    def __str__(self):
        return "%s's info" % self.user_id


class UserSetting(db.Model, ModelMixin):
    STATUS_ALLOW_ALL = '0'
    STATUS_ALLOW_AUTHENTICATED = '1'
    STATUS_ALLOW_OWN = '2'

    STATUS = (('0', _('ALLOW ALL USER')), ('1', _('ALLOW AUTHENTICATED USER')),
              ('2', _('ALLOW OWN')))

    LOCALE_CHINESE = 'zh'
    LOCALE_ENGLISH = 'en'
    LOCALE = (('zh', _('Chinese')), ('en', _('English')))

    TIMEZONE_UTC = 'UTC'
    TIMEZONE = [(i, i) for i in all_timezones]

    __tablename__ = 'usersetting'
    id = db.Column(db.Integer, primary_key=True)
    online_status = db.Column(
        db.String(10), nullable=False, default=STATUS_ALLOW_ALL)
    topic_list = db.Column(
        db.String(10), nullable=False, default=STATUS_ALLOW_ALL)
    rep_list = db.Column(
        db.String(10), nullable=False, default=STATUS_ALLOW_ALL)
    ntb_list = db.Column(
        db.String(10), nullable=False, default=STATUS_ALLOW_OWN)
    collect_list = db.Column(
        db.String(10), nullable=False, default=STATUS_ALLOW_AUTHENTICATED)
    locale = db.Column(db.String(32), nullable=False, default=LOCALE_CHINESE)
    timezone = db.Column(db.String(32), nullable=False, default=TIMEZONE_UTC)

    user_id = db.Column(
        db.Integer, db.ForeignKey(
            'user.id', ondelete="CASCADE"))
    user = db.relationship(
        User,
        backref=db.backref(
            "setting", uselist=False, cascade='all,delete', lazy='joined'),
        uselist=False,
        lazy='joined')

    def __repr__(self):
        return "<UserSetting %r>" % str(self.id)

    def __str__(self):
        return "%s's setting" % self.user_id


@event.listens_for(User, 'before_insert')
def add_info(mapper, connection, target):
    info = UserInfo()
    setting = UserSetting()
    object_session(target).add(info)
    object_session(target).add(setting)
    target.info = info
    target.setting = setting
