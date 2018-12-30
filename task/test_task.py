import unittest
from task import numbertoordinal
# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_handle_single_digits(self):
    self.assertEqual(numbertoordinal(1), "1st")

  def test_should_handle_larger_double_digits(self):
    self.assertEqual(numbertoordinal(2), "2nd")
  
  def test_should_handle_the_largest_cases(self):
    self.assertEqual(numbertoordinal(3), "3rd") 

  def test_should_handle_single_digits_like_0(self):
        self.assertEqual(numbertoordinal(0), "None")
