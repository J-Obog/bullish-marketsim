from app import db
from datetime import datetime

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    equity_prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=20000.00)
    portfolio_equity = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=0.00)
    buying_power = db.Column(db.Float(decimal_return_scale=2), nullable=False, default=20000.00)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class AccountData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    equity_prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    portfolio_equity = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    account = db.relationship('Account')