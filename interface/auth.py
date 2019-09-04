from .Base import BaseInterface
from CONFIG import BASE_URL
import requests


class Auth(BaseInterface):

    def login(self, username, password):
        headers = self._get_headers()
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(BASE_URL+'/post', headers=headers, json=data)
        if response.status_code == 200:
            self.token = response.json()['data']   # 登录成功后自动保存token
        return response

    def register(self, username, password):
        headers = self._get_headers()
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(BASE_URL + '/post', headers=headers, json=data)
        return response

    def logout(self):
        headers = self._get_headers(includes='token')
        response = requests.delete(BASE_URL + '/delete', headers=headers)
        if response.status_code == 200:
            self.token = ''   # 登出后自动保存token
        return response
