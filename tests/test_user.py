import unittest
from blog.db_class import User

class UserTest(unittest.TestCase):
  '''
  test class containing test case functions for all function in User model
  '''
  def setUp(self):
    '''
    creates a user object for  testing purposes
    '''
    self.new_user=User(username='pyra',email='pyra@yahoo.com',pass_secure='pere',bio='software engineer',profile_pic_path='photos/pyra.jpg')

  def test_setting_password(self):
    '''
    testcase to test on setting a new password
    '''
    self.assertFalse(self.new_user.pass_secure is None)

  def test_no_access_to_passwd(self):
    '''
    testcase to test that no can access a password from the database
    '''
    if self.new_user.pass_secure:
      return self.assertRaises(AttributeError)

    else:
      return self.assertRaises('False')  

  def test_password_verify(self):
    '''
    testcase to check verifying of hashed password  to login a user
    '''
    self.assertTrue(self.new_user.verify_password,('pere'))    


