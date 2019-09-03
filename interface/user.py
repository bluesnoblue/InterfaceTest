from .Base import BaseInterface
from CONFIG import BASE_URL
import requests


class User(BaseInterface):

    def get_profile(self):
        headers = self._get_headers(includes='token')
        response = requests.get(BASE_URL + '/get', headers=headers)
        return response

    def get_profile_bug(self):
        headers = self._get_headers(includes='token')
        response = requests.get(BASE_URL + '/post', headers=headers)  # bug here
        return response
