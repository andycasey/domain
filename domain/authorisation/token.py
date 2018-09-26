
from time import time

class Token(object):

    def __init__(self, access_token, expires_in=3600, token_type="Bearer"):

        self.access_token = access_token
        self.token_type
        self.expires = time() + expires_in

        return None


    @property
    def expired(self):
        return time() >= self.expires

