from app import db, ma
from datetime import datetime
from flask_marshmallow.fields import fields
from marshmallow.validate import Length

""" Models """
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    equity_prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=20000.00)
    portfolio_equity = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=0.00)
    buying_power = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=20000.00)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    account_data = db.relationship('AccountData', backref='account')

class AccountData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equity_prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    portfolio_equity = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

""" Schemas """
class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'equity_prev_close', 'portfolio_equity', 'buying_power', 'created_at')
    email = fields.Str(required=True)
    password = fields.Str(required=True, validate=Length(min=8))

class AccountDataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'account_id', 'equity_prev_close', 'portfolio_equity', 'timestamp')