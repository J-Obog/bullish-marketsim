from flask import Flask
import jinja_partials
#views
from bullish.accounts.views import accounts_router 

def create_app():
  app = Flask(__name__)
  jinja_partials.register_extensions(app)
  app.register_blueprint(accounts_router, url_prefix="/accounts")

  return app
