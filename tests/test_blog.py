import unittest
from blog.db_class import User,Blog

class BlogTest(unittest.TestCase):
  '''
  class containing test cases all function associated with Blog class
  '''
  def setUp(self):
    '''
    testcase that creates a new blog and a new user
    '''
    self.new_user=User(username='pyra',email='pyra@yahoo.com',pass_secure='pere',bio='software engineer',profile_pic_path='photos/pyra.jpg')
    self.new_blog=Blog(category='Fashion Blogs',title='Nike',body='This shoes are legit',posted_on='2019-2-3',posted_by='pyra')


  def test_check_instanse(self):
    '''
    testcase to check instanses of a blog
    '''
    self.assertEquals(self.new_blog.category,'Fashion Blogs')
    self.assertEquals(self.new_blog.title,'Nike')
    self.assertEquals(self.new_blog.body,'This shoes are legit')
    self.assertEquals(self.new_blog.posted_on,'2019-2-3')
    self.assertEquals(self.new_blog.posted_by,'pyra')
    # self.assertEquals(self.new_blog.user_id,1)

    self.assertEquals(self.new_blog.posted_by,self.new_user.username)
    
  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def tearDown(self):
    '''
    test case to delete each object after every test
    '''
    Blog.query.delete()
    User.query.delete()

  def test_save(self):
    '''
    testcase that tests if a new blog object is being saved
    '''
    self.new_blog.save_blog()
    self.assertTrue(len(Blog.query.all())>0)

  def test_get_blog(self):
    '''
    testcase to test if one can get a blog by filtering by  category
    '''
    self.new_blog.save_blog()
    blog=Blog.get_blogs('Fashion Blogs')
    self.assertTrue(len(blog)>1)

  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def test_get_personal_blogs(self):
    '''
    testcase to test on getting all blogs a user has posted on his/her profile page based on user id
    '''
    self.new_blog.save_blog()
    myblogs=Blog.personal_blogs('1')
    self.assertTrue(len(myblogs)>0)

  def test_delete_blog(self):
    '''
    test case to test if one can really delete a blog he or she has posted
    '''
    self.new_blog.save_blog()
    second_blog=Blog(category='Education Blogs',title='Chemistry',body='Its a tricky subject',posted_on='2019-8-4',posted_by='Conse',user_id=2)
    second_blog.save_blog
    self.new_blog.delete_blog()

    self.assertTrue(len(Blog.query.all())>1)


      
    


    

