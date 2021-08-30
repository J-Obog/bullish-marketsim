from api import db, ma
from flask_marshmallow.fields import fields

class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()

class UserSchema(ma.Schema):
    _id = fields.String(attribute="mongo_id")
    class Meta:
        additional = ("username", "password", "email")

user_schema = UserSchema()