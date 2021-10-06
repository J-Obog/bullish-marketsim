from app import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(6), nullable=False)
    company = db.Column(db.String(120), unique=True, nullable=False)
    prev_close = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    market_price = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    logo_url = db.Column(db.Text, nullable=False)