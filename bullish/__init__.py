from flask import Flask, render_template
#from bullish.views import 
import jinja_partials

def create_app():
  app = Flask(__name__)
  #app.register_blueprint()
  jinja_partials.register_extensions(app)
  
  

  @app.route('/')
  def index():
    return render_template('accounts.html')
  
  @app.route('/test')
  def test():
    return render_template('base.html') 

  return app
