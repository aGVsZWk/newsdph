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
