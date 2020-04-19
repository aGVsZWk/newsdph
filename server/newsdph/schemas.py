from marshmallow import Schema, fields, validates, ValidationError
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class AuthLoginSchema(Schema):
    id = fields.Int(dump_only=True)
    confirmed = fields.Boolean(dump_only=True)
    locked = fields.Boolean(dump_only=True)
    active = fields.Boolean(dump_only=True)
    username = fields.Str(load_only=True)
    password = fields.Str(load_only=True)
    remember = fields.Boolean(load_only=True)

class AuthVerifySchema(Schema):
    email = fields.Email(load_only=True)

class AuthRegisterSchema(Schema):
    name = fields.Str(load_only=True)
    email = fields.Email(load_only=True)
    username = fields.Str(load_only=True)
    password = fields.Str(load_only=True)
    code = fields.Str(load_only=True)

class UserProfileSchema(Schema):
    name = fields.Str(dump_only=True)
    sex = fields.Str(dump_only=True)
    hobby = fields.Str(dump_only=True)
    age = fields.Str(dump_only=True)
    birthday = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    address = fields.Str(dump_only=True)
    phone = fields.Str(dump_only=True)
    avatar = fields.Str(dump_only=True)
    locked = fields.Str(dump_only=True)
    role_id = fields.Str(dump_only=True)
