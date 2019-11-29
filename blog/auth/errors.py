from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def fourOfour(error):
  '''
  view function rendering 404 error page when it picks a 404 error
  '''
  return render_template('errorFour.html'),404

