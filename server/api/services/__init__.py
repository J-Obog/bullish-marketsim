from flask import Blueprint

# blueprints
import api.services.users as users
import api.services.auth as auth
import api.services.stocks as stocks

# main router
router = Blueprint("api", __name__)

# subroutes
router.register_blueprint(users.router, url_prefix="/users")
router.register_blueprint(stocks.router, url_prefix="/stocks")
router.register_blueprint(auth.router, url_prefix="/auth")