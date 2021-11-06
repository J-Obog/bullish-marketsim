from flask import Blueprint
from .controller import get_stock, get_stock_trading_data, filter_stocks

stock_bp = Blueprint('stock', __name__)
stock_bp.add_url_rule('/', view_func=filter_stocks, methods=['GET'])
stock_bp.add_url_rule('/<int:id>', view_func=get_stock, methods=['GET'])
stock_bp.add_url_rule('/<int:id>/data', view_func=get_stock_trading_data, methods=['GET'])