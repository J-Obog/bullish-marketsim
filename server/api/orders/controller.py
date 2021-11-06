from api import accounts, stocks
from flask_jwt_extended import jwt_required, current_user
from flask import jsonify
from app import db
from .model import Order, OrderSchema


@jwt_required()
def get_account_orders():
    orders = Order.query.filter_by(account_id=current_user.id).all()
    res = OrderSchema(many=True).dump(orders)
    return jsonify(data=res) 


@jwt_required()
def create_new_order():
    return {} 