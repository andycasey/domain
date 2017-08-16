# -*- coding: utf-8 -*-

import logging
import os

from .packages import (AgentsListingsPackage, PropertyLocationPackage, permissions)


__all__ = ["BaseDomainClient"]

class BaseDomainClient(object):

    """ A base object to access the Domain client API. """

    _API_URL = "https://api.domain.com.au"
    _API_VERSION = 1
    
    def __init__(self, auth_property=None, auth_agent=None):
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

        self._tokens = []
        return None


    @property
    def tokens(self):
        """ Return the existing authenticated tokens for this client. """
        return self._tokens


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

        scope, accessible_plans = permissions(end_point)

        # Do we have a token for an accessible plan with this scope already?
        for token in self.tokens:
            if scope in token.scopes and isinstance(plan, accessible_plans):
                break
        else:
            # Need to create a new token.
            for plan, credentials in self._auth.items():
                if scope in plan.available_scopes and plan in accessible_plans:
                    token = plan(credentials[0], credentials[1], scope)
                    self._tokens.append(token)
                    break
            else:
                raise ValueError("no plans available with required scope")

        return (token.session, self._api_url(end_point))


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