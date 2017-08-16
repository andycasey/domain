# -*- coding: utf-8 -*-

from .base import BasePackage

__all__ = ["PropertyLocationPackage", "PropertyLocationBusinessPackage"]


class PropertyLocationPackage(BasePackage):

    """ 
    An object to make API requests using a free 'Property and Locations' package.

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    available_scopes = (
        "api_addresslocators_read",
        "api_demographics_read",
        "api_properties_read",
        "api_listings_read",
        #"api_propertyreports_read"
        "api_salesresults_read",
        "api_suburbperformance_read"
    )


class PropertyLocationBusinessPackage(PropertyLocationPackage):

    """ 
    An object to make API requests using a business plan of a
    'Property and Locations' package.

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    pass