import unittest
from poet.user import User
from unittest.mock import patch

# https://codefather.tech/blog/write-unit-test-python/

class TestUser(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        self.user = User()
        super().__init__(*args, **kwargs)

    def test_user_activation(self):
        self.user.activate()
        self.assertEqual(self.user.is_active(), True)

    def test_user_points_update(self):
        self.user.add_points(25)
        self.assertEqual(self.user.get_points(), 25)

    def test_user_level_change(self):
        self.user.add_points(201)
        self.assertEqual(self.user.get_level(), 2)

        self.user.add_points(100)
        self.assertEqual(self.user.get_level(), 3)


# When use python file.py
# if __name__ == '__main__':
#     unittest.main()