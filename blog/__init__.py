from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_mail import Mail



login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

db=SQLAlchemy()
bootstrap=Bootstrap()
simple=SimpleMDE()
mail=Mail()

photos=UploadSet('photos',IMAGES)


def create_app(config_name):
  '''
  function responsible for registering blueprints and instances of imports
  '''
  app=Flask(__name__)
  app.config.from_object(config_options[config_name])

  db.init_app(app)
  bootstrap.init_app(app)
  login_manager.init_app(app)
  simple.init_app(app)
  mail.init_app(app)
  
  
  
  configure_uploads(app,photos)
  

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .request import configure_request
  configure_request(app)
  

  return app
  

