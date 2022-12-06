import logging
import yaml
import requests

from .utils import uri
from .authorisation.client_credentials import ClientCredentials

__all__ = ["BaseDomainClient"]

class BaseDomainClient(object):

    """ A base object to access the Domain client API. """

    def __init__(self, credentials_path, **kwargs):
        r"""
        Initialize a client with the Domain API.
        """

        # Load the credentials.
        with open(credentials_path, "r") as fp:
            contents = yaml.load(fp, Loader=yaml.FullLoader)

        self._credentials = [ClientCredentials(self, **ea) for ea in contents]

        if len(self._credentials) < 1:
            logging.warn("No API credentials found!")

        return None


    def _auth_uri(self, end_point):
        kwds = dict(host=self._AUTH_HOST,
                    version=self._AUTH_VERSION,
                    scheme=self._AUTH_SCHEME)
        return uri(end_point, **kwds)


    def _api_url(self, end_point):
        r"""
        Return the complete URL for the given API end point.

        :param end_point:
            The relative URL of the API end point.
        """
        kwds = dict(host=self._API_HOST,
                    version=self._API_VERSION,
                    scheme=self._API_SCHEME)
        return uri(end_point, **kwds)


    def _api_request(self, end_point, token, **kwargs):
        r"""
        Execute an API request to the Domain API.

        :param end_point:
            The relative URL of the API end point.
        """

        session = requests.session()
        session.headers.update(token.headers)

        r = session.get(self._api_url(end_point), **kwargs)
        if not r.ok:
            r.raise_for_status()
        return r.json()
