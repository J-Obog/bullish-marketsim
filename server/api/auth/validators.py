from marshmallow import Schema, fields, post_load, ValidationError
from api.accounts.model import Account

class AccountReq(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @post_load
    def enve(self, data, **kwargs):
        if Account.query.filter_by(email=data['email']).first():
            raise ValidationError('There is an existing account with that email', "email")