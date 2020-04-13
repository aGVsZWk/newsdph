from marshmallow import INCLUDE, EXCLUDE, RAISE
import uuid
from marshmallow import validates
from marshmallow import validate
from marshmallow import ValidationError
from datetime import date, datetime
from marshmallow import Schema, fields, pprint


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


bowie = dict(name="David Bowie")
ablum = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(ablum)
pprint(result, indent=2)


###
# declaring schemas
###

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.create_at = datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

###
# creating schems frin dict
###


UserSchema = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)

###
# serializing objects ("dumping")
###

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
print(result, type(result))

json_result = schema.dumps(user)
print(json_result, type(json_result))

###
# filtering output
###

summary_schema = UserSchema(only=("name", "email"))
summary_schema.dump(user)


###
# deserializing objects("loading")
###
user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
}
schema = UserSchema()
result = schema.load(user_data)
print(result, type(result))


###
# handing collections of objects
###
user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dumps(users)
print(result)

schema2 = UserSchema()
result2 = schema.dump(users, many=True)
print(result2)

###
# validation
###

try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)
    print(err.valid_data)


class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()


user_data = [
    {"email": "mick@stones.com", "name": "Mick"},
    {"email": "invalid", "name": "Invalid"},  # invalid email
    {"email": "keith@stones.com", "name": "Keith"},
    {"email": "charlie@stones.com"},  # missing "name"
]

try:
    BandMemberSchema(many=True).load(user_data)
except ValidationError as err:
    print(err.messages)

###
# perform additional validation for a field by passing the validate argument
###


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))


in_data = {"name": "", "permission": "invalid", "age": 71}
try:
    UserSchema().load(in_data)
except ValidationError as err:
    print(err.messages)

###
# implement your own validation functions
###


def validate_quantity(n):
    if n < 0:
        raise ValidationError("Quantity must be greater than 0.")
    if n > 30:
        raise ValidationError("Quantity must not be greater than 30.")


class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)


in_data = {"quantity": 31}

try:
    result = ItemSchema().load(in_data)
except ValidationError as err:
    print(err.messages)

###
# field validators as methods
###


class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_qua(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30...")

###
# required fields
###


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={"required": "Age is required"})
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}}
    )
    email = fields.Email()


try:
    result = UserSchema().load({"email": "foo@bar.com"})
except ValidationError as err:
    print(err.messages)

###
# partial loading(you can skip required validation by passing partial)
###


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


result = UserSchema().load({"age": 42}, partial=("name",))
# OR UserSchema(partial=('name',)).load({'age': 42})
print(result)  # => {'age': 42}


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


result = UserSchema().load({"age": 42}, partial=True)
# OR UserSchema(partial=True).load({'age': 42})
print(result)  # => {'age': 42}


###
# specifying defaults(missing specifies the default deserialization value,
# default specifies the defaultnserialization value)
###


class UserSchema(Schema):
    id = fields.UUID(missing=uuid.uuid1)
    birthdate = fields.DateTime(default=datetime(2017, 9, 29))


UserSchema().load({})
UserSchema().dump({})


###
# read-only and write-only fields
###


class UserSchema(Schema):
    name = fields.Str()
    password = fields.Str(load_only=True)
    created_at = fields.DateTime(dump_only=True)


data = {"name": "Mike", "password": "foo@bar.com", "created_at": date(2019, 1, 1)}

UserSchema(unknown=EXCLUDE).load(data)
UserSchema(unknown=EXCLUDE).dump(data)


###
# specify serialization/deserialization keys
###

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key="emailAddress")


s = UserSchema()
data = {"name": "Mike", "email": "foo@bar.com"}
result = s.dump(data)
print(result)

data = {"name": "Mike", "emailAddress": "foo@bar.com"}
result = s.load(data)
print(result)


###
# implicit field creation, use fields or additional
###

class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        fields = ("name", "email", "created_at", "uppername")
        # equal
        # additional = ("name", "email", "created_at")


user_data = {
    "name": "luke",
    "email": "a@a.c",
    "created_at": date(2010, 1, 1),
    # "uppername": "luke"
}

result = UserSchema().load(user_data)
result
