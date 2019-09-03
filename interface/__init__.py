from .auth import Auth
from .user import User


class Interface(Auth, User):

    def __init__(self, username=None, password=None):
        super().__init__()
        if username and password:
            self.login(username, password)
