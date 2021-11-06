from flask import Blueprint
from .controller import create_new_order, get_account_orders

order_bp = Blueprint('order', __name__)
order_bp.add_url_rule('/', view_func=get_account_orders, methods=['GET'])
order_bp.add_url_rule('/', view_func=create_new_order, methods=['POST'])