# -*- coding: utf-8 -*-

""" Manage package and scope permissions for API end points. """

import re
from collections import OrderedDict

from .agents_listings import *
from .property_location import *

# See https://developer.domain.com.au/docs/read/Reference for details

# TODO: Unclear what plan is required for /propertyReports

_REQUIRED_PLANS = [
    ("addressLocators", (PropertyLocationBusinessPackage, )),
    ("agencies", (AgentsListingsPackage, )),
    ("me\/agencies", 
            (PropertyLocationBusinessPackage, AgentsListingsBusinessPackage)),
    ("agents", (AgentsListingsPackage, )),
    ("demographics", (PropertyLocationBusinessPackage, )),
    ("disclaimers", (PropertyLocationBusinessPackage, )),
    # Note listings/statistics first because it needs business plans
    ("listings\/statistics", (AgentsListingsBusinessPackage, )),
    ("listings\/commercial", (AgentsListingsPackage, )),
    ("listings", (AgentsListingsPackage, )),
    ("properties", (PropertyLocationPackage, AgentsListingsBusinessPackage)),
    ("properties\/.s+\/priceEstimate", 
        (PropertyLocationBusinessPackage, AgentsListingsBusinessPackage)),
    ("properties\/_suggest", 
        (PropertyLocationPackage, AgentsListingsBusinessPackage)),
    ("salesResults", (PropertyLocationPackage, )),
    ("suburbPerformanceStatistics", (PropertyLocationBusinessPackage, )),        
]

_REQUIRED_SCOPES = {
    "addressLocators": "api_addresslocators_read",
    "agencies": "api_agencies_read",
    "agents": "api_agencies_read",
    "demographics": "api_demographics_read",
    "disclaimers": "api_properties_read",
    "listings": "api_listings_read",
    "me": "api_agencies_read",
    "properties": "api_properties_read",
    "propertyReports": "api_propertyreports_read",
    "salesResults": "api_salesresults_read",
    "suburbPerformanceStatistics": "api_suburbperformance_read"
}

def permissions(api_end_point):
    r"""
    Return the required scope and suitable packages that can access a given API
    end point.

    :param api_end_point:
        The relative URL of the API end point.

    :returns:
        A two-length tuple containing: the scope required, and a tuple of 
        suitable packages that can access the given end point.
    """

    api_end_point = api_end_point.lstrip("/")
    base_point = api_end_point.split("/")[0]
    required_scope = _REQUIRED_SCOPES.get(base_point, None)
    if required_scope is None:
        raise ValueError("no API scope recognised for end point {} ({})"\
            .format(base_point, api_end_point))

    for pattern, suitable_packages in _REQUIRED_PLANS:
        if re.match(pattern, api_end_point): break
    else:
        raise ValueError(
            "no suitable package found for end point {}".format(api_end_point))

    return (required_scope, suitable_packages)