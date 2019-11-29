import os
class Config:
  '''
  class containing the general configurations
  '''
  
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/blog'
  SECRET_KEY=os.environ.get('SECRET_KEY')

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