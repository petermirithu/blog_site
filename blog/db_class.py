from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  '''
  function that queries the database to check if user exists
  '''
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
  '''
  class defining the table holding users data
  '''
  __tablename__='users'

  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255), unique=True,index=True)
  pass_secure=db.Column(db.String())
  bio=db.Column(db.String(255))
  profile_pic_path=db.Column(db.String())
  blog=db.relationship('Blog',backref='Blog',lazy='dynamic')

  @property
  def password(self):
    '''
    function that raises an attribute error when someone tries to access the password field
    '''
    raise AttributeError('You have no access to passwords')

  @password.setter
  def password(self,password):
    '''
    function that generates hashes for a password then stores it in the db.
    '''
    self.pass_secure=generate_password_hash(password)

  def verify_password(self,password):
    '''
    function that check the hashed password in db and the login password if the are same
    '''
    return check_password_hash(self.pass_secure,password)

  def __repr__(self)  :
    '''
    function that helps in debugging.
    '''
    return f'User {self.username}'

class Blog(db.Model):
  '''
  class defining how the blog table looks and how data is stored
  '''
  __tablename__='blogs'

  id=db.Column(db.Integer,primary_key=True)
  category=db.Column(db.String(255))
  title=db.Column(db.String(255))
  body=db.Column(db.String())
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  posted_by=db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  comment=db.relationship('Comment',backref='comment',lazy='dynamic')

  def save_blog(self):
    '''
    function that saves a new blog to the database
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_blogs(cls,category):
    '''
    function that gets blogs by category
    '''    
    blogs=Blog.query.filter_by(category=category).all()
    return blogs

  @classmethod
  def personal_blogs(cls,user_id):
    '''
    function that gets all blogs posted by a signle person
    '''
    personalblogs=Blog.query.filter_by(user_id=user_id).all()
    return personalblogs

  def delete_blog(self):
    '''
    function that deletes a comment from the database
    '''
    db.session.delete(self)
    db.session.commit()

  def __repr__(self)  :
    '''
    function that helps in debugging.
    '''
    return f'Blog {self.title}'
    

class Comment(db.Model):
  '''
  class that defines comment table and how data is to be stored
  '''
  __tablename__='comments'

  id=db.Column(db.Integer,primary_key=True)
  body=db.Column(db.String(255))
  posted_by=db.Column(db.String(255))
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  blog_id=db.Column(db.Integer,db.ForeignKey('blogs.id'))

  def save_comment(self):
    '''
    function that saves a new comment to the database
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    '''
    function that gets comments for a particular blog  
    '''
    comments=Comment.query.filter_by(blog_id=id).all()
    return comments

  def delete_comment(self):
    '''
    function that deletes a comment from the database
    '''
    db.session.delete(self)
    db.session.commit()


  def __repr__(self)  :
    '''
    function that helps in debugging.
    '''
    return f'Comment {self.body}'

class Subscribe(db.Model):
  '''
  class defining how users data who have subscribed will be stored
  '''
  __tablename="subscribes"
  id=db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(255), unique=True,index=True)

  def save_subscriber(self):
    '''
    function that saves a subscriber in the db  
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_subscribers(cls):
    '''
    function that retrives all emails in subscribe table
    '''
    subscribers=Subscribe.query.all()
    return subscribers
    

  def __repr__(self)  :
    '''
    function that helps in debugging.
    '''
    return f'Comment {self.body}'

class Quote:
  '''
  class that defines instances for a quote
  '''
  def __init__(self,author,quote):
    self.author=author
    self.quote=quote
    
  








