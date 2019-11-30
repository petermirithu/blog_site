from flask import render_template,redirect,url_for,request,abort
from . import main
from flask_login import login_required,current_user
from ..db_class import User,Blog,Comment,Subscribe
from .. import db,photos
from .forms import U_profileForm,blogForm,commentForm,subscribeForm
import markdown2
from ..request import get_quotes
from ..email import mail_message

@main.route('/')
def index():
  '''
  view function that renders the home page on start up
  '''
  quote=get_quotes()
  title='Blog_Site'
  return render_template('index.html', title=title,quote=quote)

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
    new_body=form.form_body.data
    body_format= markdown2.markdown(new_body,extras=["code-friendly", "fenced-code-blocks"])

    new_blog=Blog(category=category,title=title,body=body_format,posted_by=current_user.username,user_id=current_user.id)
    new_blog.save_blog()
            
    # subscribers=Subscribe.get_subscribers()  

    # if subscribers is None:
      # abort(404)

    # else:
      # for sub in subscribers:        
        # mail_message("A new Blog Posted Check it out","email/new_blog",sub.email,sub=sub)


    return redirect(url_for('main.blog', category=category))

  return render_template('new_blog.html',form=form)  

@main.route('/blog/<int:id>/update', methods=['GET','POST'])  
@login_required
def update_blog(id):
  '''
  view function tha renders the update blog page indorder to update a blog
  '''
  blog_found=Blog.query.filter_by(id=id).first()    
  
  if blog_found is None:
    abort(404)

  form=blogForm()
  if form.validate_on_submit():
    blog_found.category=form.category.data
    blog_found.title=form.title.data      
    blog_found.body=markdown2.markdown(form.form_body.data,extras=["code-friendly", "fenced-code-blocks"])         
    
    db.session.add(blog_found)
    db.session.commit()

    return redirect(url_for('main.blog',category=blog_found.category))

  title="Update Blog"
  return render_template('updateblog.html',form=form,title=title)  

@main.route('/profile/<name>', methods=['GET','POST'])
def profile(name):
  '''
  view function that renders the profile page once triggered
  '''
  user=User.query.filter_by(username=name).first()
  personalblogs=Blog.personal_blogs(user.id)
  
  if user is None:
    abort(404)

  form=subscribeForm()

  if form.validate_on_submit():

    new_sub=Subscribe(email=form.email.data)

    new_sub.save_subscriber()

    return redirect(url_for('main.profile',name=current_user.username))

  title='Profile'
  quote=get_quotes()
  return render_template('profile/profile.html',title=title,user=user,personalblogs=personalblogs,form=form,quote=quote)  

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
  blog_Com=Blog.query.filter_by(id=id).first()
  blog_by=blog_Com.posted_by

  if form.validate_on_submit():
    body=form.body.data

    new_comment=Comment(body=body,posted_by=current_user.username,blog_id=id)

    new_comment.save_comment()

    return redirect(url_for('.comments',id=id))


  title="Comments"
  comments=Comment.get_comments(id)

  return render_template('comments.html',title=title,comments=comments,form=form,blog_by=blog_by)

@main.route('/delComment/<int:id>')
@login_required
def delComment(id):
  '''
  view function that deletes a comment if only the comment belongs to the current user
  '''
  
  comment=Comment.query.filter_by(id=id).first()

  comment.delete_comment()

  return redirect(url_for('main.comments',id=comment.blog_id))

@main.route('/delBlog/<int:id>')
@login_required
def delBlog(id):
  '''
  view function that deletes a blog if only the blog belog belongs to the current user
  '''
  
  blog_del=Blog.query.filter_by(id=id).first()

  blog_del.delete_blog()

  return redirect(url_for('main.blog',category=blog_del.category))















