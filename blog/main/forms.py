from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class blogForm(FlaskForm):
  '''
  class defining how the blog form shall look like
  '''
  category=SelectField(u'Enter Category of blog', choices =[('Lifestyle Blogs','Lifestyle Blogs'),('Entertainment Blogs','Entertainment Blogs'),('Education Blogs','Education Blogs'),('Political Blogs','Political Blogs'),('Relationship Blogs','Relationship Blogs')])
  title=StringField("Enter Blog's Title", validators=[Required()])
  body=TextAreaField('Write the blog')
  submit=SubmitField('Post')

class U_profileForm(FlaskForm):
  '''
  class defining how an update profile form shall look like
  '''
  bio=TextAreaField('Enter you Bio', validators=[Required()])
  submit=SubmitField('Submit')

class commentForm(FlaskForm):
  '''
  class that defines hopw the comment form shall look like
  '''
  body=TextAreaField('Enter your comment', validators=[Required()])
  submit=SubmitField('Post Comment')
  
