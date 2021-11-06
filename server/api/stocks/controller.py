from flask import jsonify
from .model import Stock, StockSchema, StockData, StockDataSchema

def filter_stocks():
    return jsonify(message='sme stocks')


def get_stock(id):
    stock = Stock.query.filter_by(id=id).one_or_none()
    
    if stock:
        res = StockSchema().dump(stock)
        return jsonify(res)
    
    return {}, 400


def get_stock_trading_data(id):
    stock_data = StockData.query.filter_by(stock_id=id).all()

    if stock_data:
        res = StockDataSchema(many=True).dump(stock_data)
        jsonify(data=res)

    return {}, 400