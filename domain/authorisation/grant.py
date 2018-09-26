
from collections import deque
from time import (sleep, time) # yea it is

from .packages import (scopes, throttle_rates)


class AuthorisationGrant(object):

    def __init__(self, client_id, client_secret, package=None, 
                 throttle_rate=None):

        self._client_id = client_id
        self._client_secret = client_secret
        self.package = package
        # TODO: Validate package.
        #       If we need to discover package, log a warning.

        # Automagically handle throttling.
        if throttle_rate is None:
            throttle_rate = throttle_rates[self.package]

        self._api_call_times = deque()
        self._api_throttle_rate = int(throttle_rate)


    def discover_package(self):
        r"""
        Discover which package is associated with this authorisation.
        """
        raise NotImplementedError("nope")


    @property
    def token_headers(self):
        r""" Return the authorization token for Domain. """

        # If necessary, throttle this request so Domain does not kill us.
        if self._api_throttle_rate > 0:
            while len(self._api_call_times) > self._api_throttle_rate \
            and (time() - self._api_call_times[-self._api_throttle_rate]) < 1:
                self._api_call_times.popleft()
                sleep(1) 

        self._api_call_times.append(time())

        return dict([
            ("Authorization", f"{self.token}"),
            ("Content-Type", "application/json"),
        ])




    @property
    def token(self):
        # do we have a token.

        # if not, create one with full scope.

        raise a


    @property
    def scopes(self):
        return scopes[self.package]


    def has_scope(self, scope):
        return scope in self.scopes
