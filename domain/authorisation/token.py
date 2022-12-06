
from collections import deque
from time import (sleep, time) # yea it is


class Token(object):

    def __init__(self, access_token, scope, expires_in, token_type="Bearer",
                 throttle_rate=2):

        self.access_token = access_token
        self.token_type = token_type
        self.expires = time() + expires_in
        self.scope = tuple(scope.split(" "))

        # Automagically handle throttling.
        self._api_call_times = deque()
        self._api_throttle_rate = int(throttle_rate)
        return None


    @property
    def expired(self):
        return time() >= self.expires

    def __repr__(self):
        return f"{self.token_type} {self.access_token}"

    def has_scope(self, scope):
        return scope in self.scope

    def has_any_scope(self, scopes):
        return len(set(scopes).intersection(self.scope)) > 0


    @property
    def headers(self):
        r""" Return the authorization token for Domain. """

        # If necessary, throttle this request so that Domain does not kill us.
        if self._api_throttle_rate > 0:
            while len(self._api_call_times) > self._api_throttle_rate \
            and (time() - self._api_call_times[-self._api_throttle_rate]) < 1:
                self._api_call_times.popleft()
                sleep(1) 

        self._api_call_times.append(time())

        return dict([
            ("Authorization", f"{self}"),
            ("Content-Type", "application/json"),
        ])

