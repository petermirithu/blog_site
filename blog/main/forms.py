from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email
from ..db_class import Subscribe

class blogForm(FlaskForm):
  '''
  class defining how the blog form shall look like
  '''
  category=SelectField(u'Enter Category of blog', choices =[('Lifestyle Blogs','Lifestyle Blogs'),('Entertainment Blogs','Entertainment Blogs'),('Education Blogs','Education Blogs'),('Religious Blogs','Religious Blogs'),('Political Blogs','Political Blogs'),('Fashion Blogs','Fashion Blogs')])
  title=StringField("Enter Blog's Title", validators=[Required()])
  form_body=TextAreaField('Write the blog')
  submit=SubmitField('Post')

class U_profileForm(FlaskForm):
  '''
  class defining how an update profile form shall look like
  '''
  bio=TextAreaField('Enter you Bio', validators=[Required()])
  submit=SubmitField('Submit')

class commentForm(FlaskForm):
  '''
  class that defines how the comment form shall look like
  '''
  body=TextAreaField('Enter your comment', validators=[Required()])
  submit=SubmitField('Post Comment')

class subscribeForm(FlaskForm):
  '''
  class that defines how the subscribe form shall look like
  '''
  email=StringField('Enter your email address',validators=[Required(),Email()])
  submit=SubmitField('Subscribe')  

  def validate_email(self,data_field):
    '''
    function that validates no email duplicates
    '''
    if Subscribe.query.filter_by(email=data_field.data).first():
      raise ValidationError('That Email is taken.Please use another email')

