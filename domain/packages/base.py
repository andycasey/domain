# -*- coding: utf-8 -*-

import requests
from time import time

__all__ = ["BasePackage"]

class BasePackage(object):

    """ A base object for a Domain API package. """

    available_scopes = ()

    def __init__(self, client_id, client_secret, scopes=None):
        r"""
        Initialize a BasePackage. 

        See https://developer.domain.com.au/docs/read/Packages for details on
        available API packages through the Domain API.

        :param client_id:
            A valid client ID for a package to access the Domain API.

        :param client_secret:
            A valid client secret for a package to access the Domain API.

        :param scopes: [optional]
            The API scopes requested. If `None` is selected, then all available
            scopes will be requested at the authentication step.
        """

        scopes = scopes or self.available_scopes
        if isinstance(scopes, str):
            scopes = [scopes]

        r = requests.post(
            "https://auth.domain.com.au/v1/connect/token",
            auth=(client_id, client_secret),
            data=dict(grant_type="client_credentials", scope=" ".join(scopes)))
        
        if not r.ok:
            r.raise_for_status()

        self._created = time()
        self._scopes = tuple(scopes)
        self._access_token = r.json()
        self._session = None
        return None


    @property
    def scopes(self):
        """ Return the authorized scopes for this API package. """
        return self._scopes


    @property
    def is_token_valid(self):
        """ Return whether this API token is still valid or not. """
        return self._created + self._access_token["expires_in"] >= time()


    @property
    def token(self):
        """ Return an authorised API token as a header string. """
        return "{} {}".format(
            self._access_token["token_type"],
            self._access_token["access_token"]
        )


    @property
    def session(self):
        """ Return an session that is authorised for this API package. """
        if self._session is None:
            self._session = requests.session()
            self._session.headers.update({
                "Authorization": self.token,
                "Content-Type": "application/json"
            })
        return self._session