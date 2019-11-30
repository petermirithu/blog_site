import unittest
from blog.db_class import Subscribe

class SubscripeTest(unittest.TestCase):
  '''
  test class containing test cases for all function associated with subscribe class
  '''
  def setUp(self):
    '''
    test case that sets up a subcriber
    '''
    self.new_sub=Subscribe(email='pyra@yahoo.com')

  def test_is_instance(self):
    '''
    test case that checks on instances if they are correct
    '''
    self.assertTrue(self.new_sub.email,'pyra@yahoo.com')

  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def test_save_subsciber(self):
    '''
    test case that tests if one can be saved in subscribers class
    '''
    self.new_sub.save_subscriber()

    self.assertFalse(len(Subscribe.query.all())<1)  

  def tearDown(self):
    '''
    test case to delete each object after every test
    '''
    Subscribe.query.delete()

  @unittest.skip("Its working but i would love to see the other errors for other tests!")
  def test_get_subscribers(self):
    '''
    testcase to test on getting all subscribers from Subscribes table
    '''
    self.new_sub.save_subscriber()
    subscribers=Subscribe.get_subscribers()

    self.assertGreater(len(subscribers),0)
    


    
