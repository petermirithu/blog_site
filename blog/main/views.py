from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from ..db_class import User,Blog,Comment
from .. import db
import markdown2

@main.route('/')
def index():
  '''
  view function that renders the home page on start up
  '''
  title='Blog_Site'
  return render_template('index.html', title=title)

# @main.route('/blog')