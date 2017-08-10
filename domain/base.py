# -*- coding: utf-8 -*-

import logging
import os
import requests
from time import time

from . import __version__

__all__ = ["BaseDomainClient"]


class Token(object):
    def __init__(self, access_token, expires_in, token_type):
        self._access_token = access_token
        self._expires_in = expires_in
        self._token_type = token_type
        self._expires_at = time() + expires_in

    @property
    def expired(self):
        return time() >= self._expires_at

    def __repr__(self):
        return "{} {}".format(self._token_type, self._access_token)



class BaseDomainClient(object):

    def __init__(self, client_id=None, client_secret=None):
        r"""
        Initialize a BaseDomainClient.

        :param client_id: [optional]
            The `client_id` to use to authorise this application with the Domain
            Property API. If `None` is supplied then the value will be read from
            the `DOMAIN_LISTINGS_API_KEY` environment variable.

        :param client_secret: [optional]
            The `client_secret` to use to authorise this application with the
            Domain Property API. If `None` is supplied then the value will be
            read from the `DOMAIN_LISTINGS_API_SECRET` environment variable.
        """

        # Take the client_id/client_secret or default to an environment variable
        self._authorization_params = (
            client_id or os.environ.get("DOMAIN_LISTINGS_API_KEY"),
            client_secret or os.environ.get("DOMAIN_LISTINGS_API_SECRET")
        )
        if None in self._authorization_params:
            logging.warn("Incomplete authorization parameters.")

        self._session = None
        self._token = None
        return None


    @property
    def token(self):
        r"""
        Return a current bearer token from the Domain API.
        """

        # Check for an unexpired token.
        if self._token is None or self._token.expired:
            r = requests.post(
                    "https://auth.domain.com.au/v1/connect/token",
                    auth=self._authorization_params,
                    data={
                        "grant_type": "client_credentials",
                        "scope": "api_listings_read"
                    }
                )

            if not r.ok:
                r.raise_for_status()

            self._token = Token(**r.json())

        return self._token


    @property
    def session(self):

        if self._session is None:
            self._session = requests.session()
            self._session.headers.update({
                "Authorization": self.token,
                "User-Agent": "get-rich/{}".format(__version__),
                "Content-Type": "application/json"
            })
        return self._session