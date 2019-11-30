import os
class Config:
  '''
  class containing the general configurations
  '''
  
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/blog_db'
  SECRET_KEY=os.environ.get('SECRET_KEY')

  BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

  UPLOADED_PHOTOS_DEST='blog/static/photos'
  
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=587
  MAIL_USER_TLS=True
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
  '''
  class containing configrations for running the app in production mode
  '''
  pass

class DevConfig(Config):
  '''
  class containing configurations for running the app in development mode
  '''
  DEBUG=True

class TestConfig(Config):
  '''
  test class containing configrations for running the tests
  '''
  pass

config_options={
  'production':ProdConfig,
  'development':DevConfig,
  'test':TestConfig
}