from bullish import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    balance = db.Column(db.Float, default=10000.00)
    buying_power: db.Column(db.Float, default=10000.00)

class AccountData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id: db.Column(db.Integer, primary_key=True)
    price: db.Column(db.Float, primary_key=True)
    timestamp: db.Column(db.Integer, primary_key=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), unique=True, nullable=False)
    ticker = db.Column(db.String(120), unique=True, nullable=False)
    logo_url = db.Column(db.String(120), unique=True, nullable=False)
    ipo_date = db.Column(db.String(120), unique=True, nullable=False)

class StockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id: db.Column(db.Integer, primary_key=True)
    price: db.Column(db.Float, primary_key=True)
    timestamp: db.Column(db.Integer, primary_key=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, primary_key=True)
    #transaction_type: enum
    price = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, primary_key=True)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, primary_key=True)
    cost_basis = db.Column(db.Integer, primary_key=True)
    quanitity = db.Column(db.Integer, primary_key=True)
