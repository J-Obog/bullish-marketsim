from flask import Blueprint

# blueprints
from api.routes import users, stocks, auth

# main router
router = Blueprint("api", __name__)

# subroutes
router.register_blueprint(users.router, url_prefix="/users")
router.register_blueprint(stocks.router, url_prefix="/stocks")
router.register_blueprint(auth.router, url_prefix="/auth")