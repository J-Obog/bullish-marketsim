from app import db
from datetime import datetime

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(6), nullable=False)
    company = db.Column(db.String(120), unique=True, nullable=False)
    prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    market_price = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    logo_url = db.Column(db.Text, nullable=False)

class StockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    market_price = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    stock = db.relationship('Stock')