# -*- coding: utf-8 -*-

from .base import BasePackage

__all__ = ["AgentsListingsPackage", "AgentsListingsBusinessPackage"]


class AgentsListingsPackage(BasePackage):

    """ 
    An object to make API requests using the free 'Agents and Listings' package.

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    available_scopes = ("api_agencies_read", "api_listings_read")


class AgentsListingsBusinessPackage(AgentsListingsPackage):

    """ 
    An object to make API requests using a business plan edition of an
    'Agents and Listings' package.

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    available_scopes = ("api_agencies_read", "api_listings_read",
        "api_propertyreports_read")
