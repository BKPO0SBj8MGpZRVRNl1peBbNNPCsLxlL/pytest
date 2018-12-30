import unittest
from oop import user, moderator, admin
user1 = user('User 1')
mod = moderator('Moderator')

class Test(unittest.TestCase):
  def test_instantiation(self):
    self.assertEqual(user1.name,'User 1', 'User name is set correctly')
    user1.name = 'User 1 Updated'
    self.assertEqual(user1.name,'User 1 Updated', 'User name can be updated')
    self.assertIsInstance(mod, user, 'Moderator is a user')