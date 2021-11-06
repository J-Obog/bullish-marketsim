from app import db, ma
from datetime import datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_per_share = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)


""" Schema """
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'price_per_share', 'quantity', 'timestamp', 'account_id', 'stock_id')