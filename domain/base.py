# -*- coding: utf-8 -*-

import logging
import os

from .plans import (AgentListingsPlan, PropertyLocationsPlan)

__all__ = ["BaseDomainClient"]


class BaseDomainClient(object):

    _API_URL = "https://api.domain.com.au"
    _API_VERSION = 1
    

    def __init__(self, auth_property=None, auth_agent=None):
        r"""
        Initialize a BaseDomainClient.
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
            PropertyLocationsPlan: auth_property,
            AgentListingsPlan: auth_agent
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
        return self._tokens


    def _scope_required(self, end_point):

        # Get top-level endpoint.
        reference_point = end_point.lstrip("/").split("/")[0]

        # What scope is required for this reference point?
        reference_point_scopes = {
            "addressLocators": "api_addresslocators_read",
            "agencies": "api_agencies_read",
            "agents": "api_agencies_read",
            "me": "api_agencies_read",
            "demographics": "api_demographics_read",
            "disclaimers": "api_properties_read",
            "listings": "api_listings_read",
            "properties": "api_listings_read",
            "propertyReports": "api_propertyreports_read",
            "salesResults": "api_salesresults_read",
            "suburbPerformanceStatistics": "api_suburbperformance_read"
        }

        scope = reference_point_scopes.get(reference_point, None)
        if scope is None:
            raise ValueError("no API scope recognised for end point {}".format(
                reference_point))
        return scope


    def _api_url(self, end_point):
        return "{}/v{}/{}".format(self._API_URL, self._API_VERSION, end_point)


    def _prepare_request(self, end_point):

        scope = self._scope_required(end_point)

        # Do we have a token with this scope already?
        for token in self.tokens:
            if scope in token.scopes: break
        else:
            # What plan has this scope?
            for plan, credentials in self._auth.items():
                if scope in plan.available_scopes:
                    self._tokens.append(plan(credentials[0], credentials[1], scope))
                    token = self._tokens[-1]
                    break
            else:
                raise ValueError("no plans available with required scope")

        return (token.session, self._api_url(end_point))


    def _api_request(self, end_point, **kwargs):
        
        session, url = self._prepare_request(end_point)

        r = session.get(url, **kwargs)
        if not r.ok:
            r.raise_for_session()
        return r


