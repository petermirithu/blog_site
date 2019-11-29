#pylint: skip-file
from flask import render_template,url_for,request,flash,redirect
from . import auth
from .. import db
from ..db_class import User
from .forms import SignupForm,SigninForm
from flask_login import login_user,logout_user,login_required,current_user

@auth.route('/signup', methods=['GET','POST'])
def signup():
  '''
  view function that renders sign up page to allow new users in the app
  '''
  form=SignupForm()

  if form.validate_on_submit():    
    user=User(username=form.username.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.signin'))

  return render_template('auth/signup.html',form=form)

@auth.route('/signin',methods=['GET','POST'])
def signin():
  '''
  view function that renders the sign in for when called
  '''
  form=SigninForm()

  if form.validate_on_submit():
    user=User.query.filter_by(username=form.username.data).first()

    if user is None:
      flash('Please Enter your credentials')

    elif user is not None and user.verify_password(form.password.data):

      login_user(user,form.remember.data)

      return redirect(request.args.get('next') or url_for('main.index'))

  return render_template('auth/signin.html',form=form)    

@auth.route('/signout')  
@login_required
def signout():
  '''
  view function that logs out a user once called
  '''
  logout_user()
  render_template(url_for('main.index'))












