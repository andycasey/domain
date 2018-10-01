
import requests
from .scopes import package_plan_scopes
from .token import Token

class AuthorisationGrant(object):

    def __init__(self, client, client_id, client_secret, package_and_plan=None):

        self._auth = (client_id, client_secret)
        self.client = client
        self.package_and_plan = package_and_plan
        return None


    def discover_package_and_plan(self):
        r"""
        Discover which package is associated with this authorisation.
        """
        raise NotImplementedError


    @property
    def token(self):
        token = getattr(self, "_token", None)
        if token is None or token.expired:
            self._token = self.create_token()

        return self._token


    def create_token(self, scopes=None):

        if scopes is None:
            scopes = package_plan_scopes[self.package_and_plan]

        r = requests.post(
            self.client._auth_uri("connect/token"),
            auth=self._auth,
            data=dict(
                grant_type="client_credentials",
                scope=" ".join(scopes)))

        if not r.ok:
            r.raise_for_status()

        kwds = dict(scopes=scopes)
        kwds.update(r.json())

        return Token(**kwds)

