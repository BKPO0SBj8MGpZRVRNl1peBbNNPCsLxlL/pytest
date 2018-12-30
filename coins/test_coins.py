import unittest
# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_handle_the_example_case(self):
    self.assertEqual(count_change(4,[1,2]), 3)
  def test_should_handle_another_simple_case(self):
    self.assertEqual(count_change(10,[5,2,3]), 4)