# -*- coding: utf-8 -*-

from . import utils
from .base import BaseDomainClient

__all__ = ["DomainClient"]

class DomainClient(BaseDomainClient):

    """ A client for the Domain API. """

    @property
    def sales_results_metadata(self):
        r""" Retrieve metadata regarding sales result data. """
        return self._api_request("salesResults/_head")


    def sales_results(self, city):
        r"""
        Retrieve sales results for a given city.

        :param city:
            City to retrieve sales results for. Supported cities are:
            Adelaide, Brisbane, Canberra, Melbourne, Sydney.
        """
        city = utils.validate_city(city)
        return self._api_request("salesResults/{}".format(city))


    def sales_results_listings(self, city):
        r"""
        Retrieve listing summaries corresponding to the sales results.

        :param city:
            City to retrieve listing summaries for. Supported cities are:
            Adelaide, Brisbane, Canberra, Melbourne, Sydney.
        """
        city = utils.validate_city(city)
        return self._api_request("salesResults/{}/listings".format(city))


    def listing(self, listing_id):
        r"""
        Retrieve a specific property listing.

        :param listing_id:
            The listing identifier. 
        """
        return self._api_request("listings/{:.0f}".format(int(listing_id)))


    def property(self, property_id):
        r"""
        Retrieve a specific property.

        :param property_id:
            The property identifier.
        """
        return self._api_request("properties/{}".format(property_id))


    def properties(self, search_terms, limit=15, channel="all"):
        r"""
        Return properties matching the given search terms.

        :param search_terms:
            The terms to search for.

        :param limit: [optional]
            The maximum number of results to return (default: 15).

        :param channel: [optional]
            Restrict properties to a particular type. Supported types: all,
            residential, commercial. (default: 'all')
        """

        limit = int(limit)
        if 1 > limit:
            raise ValueError("limit must be a positive integer")

        channel = utils.validate_channel(channel)
        return self._api_request("properties/_suggest", params=dict(
            terms=search_terms, pageSize=limit, channel=channel))


    def agencies(self, search_terms, page_number=1, page_size=20):
        r"""
        Return a summary of agencies matching the specified criteria.

        :param search_terms:
            The terms to search for.

        :param page_number: [optional]
            The page number for paginated results (default: 1).

        :param page_size: [optional]
            The page size for paginated results (max: 500, default: 20).
        """
        return self._api_request("agencies", params=dict(q=search_terms,
            pageNumber=int(page_number), pageSize=int(page_size)))