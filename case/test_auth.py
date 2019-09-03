import unittest
from interface import Interface
from ddt import ddt, file_data
from CONFIG import TEST_USERNAME, TEST_PASSWORD


@ddt
class TestAuthBASE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global con
        con = Interface()

    @file_data('../data/test_auth_login.yaml')
    def test_login(self, username, password):
        r = con.login(username, password)
        self.assertEqual(r.status_code, 200)

    @file_data('../data/test_auth_register.yaml')
    def test_register(self, username, password):
        r = con.register(username, password)
        self.assertEqual(r.status_code, 200)

    def test_logout(self):
        con2 = Interface(username=TEST_USERNAME, password=TEST_PASSWORD)
        r = con2.logout()
        self.assertEqual(r.status_code, 200)
