from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..db_class import User

class SignupForm(FlaskForm):
  '''
  class defining how the sign up form looks like
  '''
  username=StringField('Enter Desired Username',validators=[Required()])
  email=StringField('Enter your email address',validators=[Required(),Email()])
  password=PasswordField('Enter a password', validators=[Required(),EqualTo('password_auth',message='Passwords must match')])
  password_auth=PasswordField('Confirm Password', validators=[Required()])
  submit=SubmitField('Sign Up!')

  def validate_email(self,data_field):
    '''
    function that validates no email duplicates
    '''
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('That Email is taken.Please use another email')

  def validate_username(self,data_field):
    '''
    function that validates no username duplicates
    '''
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError('That username is taken.Please be creative')


class SigninForm(FlaskForm):
  '''
  class defining how the sign in form looks like
  '''
  username=StringField('Enter your username', validators=[Required()])
  password=PasswordField('Enter your password', validators=[Required()])
  remember=BooleanField('Remember Me')
  submit=SubmitField('Sign In!')

  