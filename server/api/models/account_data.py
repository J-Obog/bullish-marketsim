from app import db 
from datetime import datetime

class AccountData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    equity_prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    portfolio_equity = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    account = db.relationship('Account')