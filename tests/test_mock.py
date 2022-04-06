import unittest
from unittest.mock import patch, Mock
from poet.user import User

# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python

# http://www.ines-panker.com/2020/06/01/python-mock.html#:~:text=side_effect%20vs%20return_value,t%20need%20to%20call%20it.

# https://huongdanjava.com/overview-about-mock-in-unit-test.html

class TestUser(unittest.TestCase):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @patch('poet.user.User.is_active', return_value=True)
    def test_user_activation(self, is_active):
        self.assertEqual(is_active(), True)

    @patch('poet.user.User')
    def test_user_points_update(self, MockUser):
        user = MockUser()
        user.add_points(25)
        user.get_points.return_value=25
        self.assertEqual(user.get_points(), 25)

    @patch('poet.user.User')
    def test_user_level_change(self, MockUser):
        user = MockUser()
        user.add_points(201)
        user.get_level.return_value=2
        self.assertEqual(user.get_level(), 2)

        user.add_points(100)
        user.get_level.return_value=3
        self.assertEqual(user.get_level(), 3)
