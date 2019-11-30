import unittest
from blog.db_class import User,Blog,Comment

class CommentTest(unittest.TestCase):
  '''
  class containing test cases all function associated with Comment class
  '''
  def setUp(self):
    '''
    testcase that creates a new comment and new blog 
    '''    
    self.new_blog=Blog(category='Fashion Blogs',title='Nike',body='This shoes are legit',posted_on='2019-2-3',posted_by='pyra')
    self.new_comment=Comment(body='I love it',posted_on='2019-7-12',posted_by='pyra')


  def test_check_instanse(self):
    '''
    testcase to check instanses of a comment
    '''    
    self.assertEquals(self.new_comment.body,'I love it')
    self.assertEquals(self.new_comment.posted_on,'2019-7-12')
    self.assertEquals(self.new_comment.posted_by,'pyra')
    # self.assertEquals(self.new_comment.blog_id,1)    

  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def tearDown(self):
    '''
    test case to delete each object after every test
    '''
    Blog.query.delete()
    Comment.query.delete()

  def test_save(self):
    '''
    testcase that tests if a new comment object is being saved
    '''
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all())>0)

  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def test_get_comment(self):
    '''
    testcase to test if one can get a comment by filtering by  blog_id
    '''
    self.new_comment.save_comment()
    comment=Comment.get_comments('1')
    self.assertTrue(len(comment)>0)
  
  def test_delete_comment(self):
    '''
    test case to test if one can really delete a comment he or she has posted
    '''
    self.new_comment.save_comment()
    second_comment=Comment(body='its dope',posted_on='2019-8-4',posted_by='Muthoni',blog_id=1)
    second_comment.save_comment
    self.new_comment.delete_comment()

    self.assertTrue(len(Comment.query.all())>1)


      
    


    

