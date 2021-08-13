from flask import Flask
import jinja_partials
#views
from bullish.routes.account_router import account_bp
from bullish.routes.accounts_router import accounts_bp

def create_app():
  app = Flask(__name__)
  jinja_partials.register_extensions(app)
  app.register_blueprint(accounts_bp, url_prefix="/")
  app.register_blueprint(account_bp, url_prefix="/account/<int:id>")

  return app
