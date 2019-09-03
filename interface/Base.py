import requests
from time import time


class BaseInterface(object):

    def __init__(self):
        self.token = ''

    def _get_headers(self, includes=''):
        t = str(int(time()))

        headers = {
            'timestamp': t,
        }

        if 'token' in includes:
            headers['token'] = self.token

        return headers
