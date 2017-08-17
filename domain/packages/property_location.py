# -*- coding: utf-8 -*-

from .base import BasePackage

__all__ = ["PropertyLocationPackage", "PropertyLocationBusinessPackage"]

class PropertyLocationPackage(BasePackage):

    """ 
    An object to make API requests using the free edition of a 
    'Property and Locations' package.

    This package has the following available scopes:

    - ``api_properties_read``
    - ``api_salesresults_read``

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    available_scopes = ("api_properties_read", "api_salesresults_read")


class PropertyLocationBusinessPackage(PropertyLocationPackage):

    """ 
    An object to make API requests using the business edition of a 
    'Property and Locations' package.

    This package has the following available scopes:

    - ``api_properties_read``
    - ``api_salesresults_read``
    - ``api_propertyreports_read``
    - ``api_suburbperformance_read``

    See https://developer.domain.com.au/docs/read/Packages for details.
    """

    available_scopes = ("api_properties_read", "api_salesresults_read",
        "api_propertyreports_read", "api_suburbperformance_read")