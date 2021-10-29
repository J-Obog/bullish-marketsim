from marshmallow import Schema, fields
from marshmallow.validate import Length

class AccountValidator(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=Length(min=8))