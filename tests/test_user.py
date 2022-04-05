import unittest
from poet.user import User
# https://codefather.tech/blog/write-unit-test-python/

class TestUser(unittest.TestCase):

    def test_user_activation(self):
        u = User()
        u.activate()
        self.assertEqual(u.is_active(), True)

    def test_user_points_update(self):
        u = User()
        u.add_points(25)
        self.assertEqual(u.get_points(), 25)

    def test_user_level_change(self):
        u = User()
        u.add_points(201)
        self.assertEqual(u.get_level(), 2)

        u.add_points(100)
        self.assertEqual(u.get_level(), 3)


# When use python file.py
# if __name__ == '__main__':
#     unittest.main()