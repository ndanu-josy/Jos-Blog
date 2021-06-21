import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='jos', email = "ndanujosie@gmail.com",password='1234')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234'))