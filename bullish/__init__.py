from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bullish.views import bp
import jinja_partials

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config.from_pyfile("config.py")
  
  #binding plugins
  db.init_app(app)
  jinja_partials.register_extensions(app)
  
  #register blueprint
  app.register_blueprint(bp)

  return app