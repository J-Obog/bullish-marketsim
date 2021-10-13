from app import db

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    cost_basis = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    account = db.relationship('Account')
    stock = db.relationship('Stock')