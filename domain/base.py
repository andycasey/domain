# -*- coding: utf-8 -*-

import logging
import os

from .packages import (AgentsListingsPackage, PropertyLocationPackage, permissions)

__all__ = ["BaseDomainClient"]

class BaseDomainClient(object):

    """ A base object to access the Domain client API. """

    _API_URL = "https://api.domain.com.au"
    _API_VERSION = 1
    
    def __init__(self, auth_property=None, auth_agent=None, limit_scopes=False):
        r"""
        Initialize a client for the Domain API.

        :param auth_property: [optional]
            A two-length tuple containing a client ID and secret for a 'Property
            and Locations' package on the Domain API. If `None` is specified, 
            then the client ID and secret will be read from the 
            `API_DOMAIN_PROPERTY_CLIENT_ID` and the `API_DOMAIN_PROPERTY_CLIENT_SECRET`
            environment variables.

        :param auth_agent: [optional]
            A two-length tuple containing a client ID and secret for the
            'Agents and Listings' package on the Domain API. If `None` is specified
            then the client ID and secret will be read from the
            `API_DOMAIN_AGENT_CLIENT_ID` and `API_DOMAIN_AGENT_CLIENT_SECRET`
            environment variables.

        :param limit_scopes: [optional]
            Restrict the API scopes only to what is needed for a request, rather
            than creating tokens with all available scopes for the given package.
            Subsequent API requests may be faster if `limit_scopes` is `False`
            (default: False).
        """

        if auth_property is None:
            auth_property = (
                os.environ.get("API_DOMAIN_PROPERTY_CLIENT_ID"),
                os.environ.get("API_DOMAIN_PROPERTY_CLIENT_SECRET")
            )

        if auth_agent is None:
            auth_agent = (
                os.environ.get("API_DOMAIN_AGENT_CLIENT_ID"),
                os.environ.get("API_DOMAIN_AGENT_CLIENT_SECRET")
            )

        self._auth = {
            AgentsListingsPackage: auth_agent,
            PropertyLocationPackage: auth_property
        }

        for k, v in self._auth.items():
            if None not in v: break
        else:
            # No break
            logging.warn("No API credentials found!")

        self._packages = []
        self._limit_scopes = limit_scopes
        return None


    @property
    def packages(self):
        """ Return the existing authenticated packages for this client. """
        return self._packages


    def _api_url(self, end_point):
        r"""
        Return the complete URL for the given API end point.

        :param end_point:
            The relative URL of the API end point.
        """
        return "{}/v{}/{}".format(self._API_URL, self._API_VERSION, end_point)


    def _prepare_request(self, end_point):
        r"""
        Return an authenticated session for a given API end point, and the 
        complete URL for that end point.

        :param end_point:
            The relative URL of the API end point.
        """

        scope, packages = permissions(end_point)

        # What scope level will we request?
        req_scope = scope if self._limit_scopes else None           

        # Do we have a token for an accessible plan with this scope already?
        for package in self.packages:
            if scope in package.scopes and isinstance(package, packages) \
            and package.is_token_valid:
                break
        else:
            # Need to create a new token.
            for plan, credentials in self._auth.items():
                if scope in plan.available_scopes and plan in packages:
                    package = plan(credentials[0], credentials[1], req_scope)
                    self._packages.append(package)
                    break
            else:
                raise ValueError("no packages available with required scope")

        return (package.session, self._api_url(end_point))


    def _api_request(self, end_point, **kwargs):
        r"""
        Execute an API request to the Domain API.

        :param end_point:
            The relative URL of the API end point.
        """

        session, url = self._prepare_request(end_point)

        r = session.get(url, **kwargs)
        if not r.ok:
            r.raise_for_status()
        return r