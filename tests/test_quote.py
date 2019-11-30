import unittest
from blog.db_class import Quote

class QuoteTest(unittest.TestCase):
  '''
  test class containing test cases for all function associated with quote class
  '''
  def setUp(self):
    '''
    test case that sets up a quote
    '''
    self.new_quote=Quote(author='Jonnes',quote='Never lose hope')

  def test_is_instance(self):
    '''
    test case that checks on instances if they are correct
    '''
    self.assertTrue(self.new_quote.author,'Jonnes')
    self.assertTrue(self.new_quote.quote,'Never lose hope')
    