import unittest
from interface import Interface
from ddt import ddt, file_data
from CONFIG import TEST_USERNAME, TEST_PASSWORD


@ddt
class TestAuthBASE(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global con
        con = Interface(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_get_profile(self):
        r = con.get_profile()
        self.assertEqual(r.status_code, 200)

    def test_get_profile_bug(self):  # bug here
        r = con.get_profile_bug()
        self.assertEqual(r.status_code, 200)
