# -*- coding: utf-8 -*-

import requests
from time import time

__all__ = ["PropertyLocationsPlan", "AgentListingsPlan"]


class BaseAPIPlan(object):

    available_scopes = ()

    def __init__(self, client_id, client_secret, scopes=None):

        scopes = scopes or self.available_scopes
        if isinstance(scopes, str):
            scopes = [scopes]

        r = requests.post(
            "https://auth.domain.com.au/v1/connect/token",
            auth=(client_id, client_secret),
            data={
                "grant_type": "client_credentials",
                "scope": " ".join(scopes)
            }
        )

        if not r.ok:
            r.raise_for_status()

        self._created = time()
        self._scopes = tuple(scopes)
        self._access_token = r.json()
        self._session = None
        return None


    @property
    def scopes(self):
        return self._scopes


    @property
    def has_token_expired(self):
        return time() >= self._created + self._access_token["expires_in"]


    @property
    def token(self):
        return "{} {}".format(
            self._access_token["token_type"],
            self._access_token["access_token"]
        )


    @property
    def session(self):
        if self._session is None:
            self._session = requests.session()
            self._session.headers.update({
                "Authorization": self.token,
                "Content-Type": "application/json"
            })
        return self._session



class PropertyLocationsPlan(BaseAPIPlan):

    available_scopes = (
        "api_addresslocators_read",
        "api_demographics_read",
        "api_properties_read",
        "api_listings_read",
        #"api_propertyreports_read"
        "api_salesresults_read",
        "api_suburbperformance_read"
    )



class AgentListingsPlan(BaseAPIPlan):

    available_scopes = (
        "api_agencies_read",
        "api_listings_read",
        #"api_propertyreports_read",
    )
