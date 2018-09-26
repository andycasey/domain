# -*- coding: utf-8 -*-

import logging
import os
import yaml
from time import (sleep, time)

from collections import (deque, OrderedDict)

from .packages import (AgentsListingsPackage, AgentsListingsBusinessPackage,
    PropertyLocationPackage, PropertyLocationBusinessPackage, permissions)

from .authorisations import ClientCredentials

__all__ = ["BaseDomainClient"]

class BaseDomainClient(object):

    """ A base object to access the Domain client API. """

    def __init__(self, credentials_path, **kwargs):
        r"""
        Initialize a client with the Domain API.
        """

        # Load the credentials.
        with open(credentials_path, "r") as fp:
            contents = yaml.load(fp)

        self._credentials = [ClientCredentials(**entry) for entry in contents]

        if len(self._credentials) < 1:
            logging.warn("No API credentials found!")

        return None


    def _api_url(self, end_point, scheme=None):
        r"""
        Return the complete URL for the given API end point.

        :param end_point:
            The relative URL of the API end point.

        :param scheme: [optional]
            The scheme to use when constructing the API URL. If None is given
            then the first available scheme will be used.
        """
        if scheme is None:
            scheme = self._API_SCHEMES[0]

        elif scheme not in self._API_SCHEMES:
            raise ValueError(f"API scheme '{scheme}' not recognised")

        host, version = self._API_HOST, self._API_VERSION

        return f"{scheme}://{host}/{version}/{end_point}"


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


    def _api_request(self, end_point, token, **kwargs):
        r"""
        Execute an API request to the Domain API.

        :param end_point:
            The relative URL of the API end point.
        """

        session, url = self._prepare_request(end_point)

        # Throttle based on package used.
        raise a

        r = session.get(url, **kwargs)
        if not r.ok:
            r.raise_for_status()
        return r.json()

