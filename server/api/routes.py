from flask import Blueprint
from api.auth import router as auth_router
from api.users import router as users_router
from api.stocks import router as stocks_router

router = Blueprint("api", __name__)

router.register_blueprint(auth_router, url_prefix="/auth")
router.register_blueprint(users_router, url_prefix="/users")
router.register_blueprint(stocks_router, url_prefix="/stocks")