from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from ..db_class import User,Blog,Comment
from .. import db,photos
from .forms import U_profileForm,blogForm,commentForm
import markdown2

@main.route('/')
def index():
  '''
  view function that renders the home page on start up
  '''
  title='Blog_Site'
  return render_template('index.html', title=title)

@main.route('/blog/<category>')
def blog(category):
  '''
  view function that renders the blog template and displays blogs based category
  '''
  title=category
  blogs=Blog.get_blogs(category)
    
  return render_template('blog.html',blogs=blogs,title=title)

@main.route('/blog/new/blog', methods=['GET','POST'])  
@login_required
def new_blog():
  '''
  view function that renders the post blog form for adding new blogs  
  '''
  form=blogForm()
  if form.validate_on_submit():
    category=form.category.data    
    title=form.title.data
    body=form.body.data
    new_body=markdown2.markdown(body,extras=["code-friendly","fenced-code-blocks"])

    new_blog=Blog(category=category,title=title,body=new_body,posted_by=current_user.username,user_id=current_user.id)
    new_blog.save_blog()

    return redirect(url_for('main.blog', category=category))

  return render_template('new_blog.html',form=form)  

@main.route('/profile/<name>')
def profile(name):
  '''
  view function that renders the profile page once triggered
  '''
  user=User.query.filter_by(username=name).first()
  personalblogs=Blog.personal_blogs(user.id)
  
  if user is None:
    abort(404)

  title='Profile'
  return render_template('profile/profile.html',title=title,user=user,personalblogs=personalblogs)  

@main.route('/profile/<name>/update', methods=['GET','POST'])
def update_profile(name):
  '''
  view function that renders the update profile page form.
  '''
  user=User.query.filter_by(username=name).first()

  if user is None:
    abort(404)

  form=U_profileForm()
  if form.validate_on_submit():
    user.bio=form.bio.data  
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('main.profile',name=user.username))

  return render_template('profile/update.html', form=form)  

@main.route('/profile/<name>/update/pic', methods=['GET','POST'])
@login_required
def update_pic(name):
  '''
  view function that pics the selected picture and saves it to the database as a path
  '''
  user=User.query.filter_by(username=name).first()
  
  if 'photo' in request.files:
    filename=photos.save(request.files['photo'])
    path=f'photos/{filename}'
    user.profile_pic_path=path
    db.session.commit()

  return redirect(url_for('main.profile', name=user.username))  

@main.route('/blog/comments/<int:id>', methods=['GET','POST'])
@login_required
def comments(id):
  '''
  view function that render comment template containing comments for a blog
  '''
  form=commentForm()
  if form.validate_on_submit():
    body=form.body.data

    new_comment=Comment(body=body,posted_by=current_user.username,blog_id=id)

    new_comment.save_comment()

    return redirect(url_for('.comments',id=id))

  blog=Blog.query.filter_by(id=id).first()
  blog_id=blog.id

  title="Comments"
  comments=Comment.get_comments(id)

  return render_template('comments.html',title=title,blog_id=blog_id,comments=comments,form=form)














