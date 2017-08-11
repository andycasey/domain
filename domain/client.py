# -*- coding: utf-8 -*-

from .base import BaseDomainClient



class Client(BaseDomainClient):

    @property
    def sales_results_metadata(self):
        r"""
        Retrieve metadata regarding sales result data.
        """
        return self._api_request("salesResults/_head").json()


    def sales_results(self, city):
        r"""
        Retrieve sales results for a given city.

        :param city:
            City to retrieve sales results for. Supported cities are:
            Adelaide, Brisbane, Canberra, Melbourne, Sydney.
        """
        city = _validate_city(city)
        return self._api_request("salesResults/{}".format(city)).json()


    def sales_results_listings(self, city):
        r"""
        Retrieve listing summaries corresponding to the sales results.

        :param city:
            City to retrieve listing summaries for. Supported cities are:
            Adelaide, Brisbane, Canberra, Melbourne, Sydney.
        """

        city = _validate_city(city)
        return self._api_request("salesResults/{}/listings".format(city)).json()


    def listing(self, listing_id):
        r"""
        Retrieve a specific property listing.

        :param listing_id:
            Listing identifier.
        """

        return self._api_request("listings/{:.0f}".format(int(listing_id))).json()
        

    def property(self, property_id):
        r"""
        Retrieve a specific property.

        :param property_id:
            The property identifier.
        """

        return self._api_request("properties/{}".format(property_id)).json()


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

        channel = _validate_channel(channel)

        return self._api_request("properties/_suggest", params=dict(
            terms=search_terms, pageSize=limit, channel=channel)).json()





def _validate_channel(channel):
    channel = channel.strip().title()
    supported_channels = ("all", "commercial", "residential")
    for supported_channel in supported_channels:
        if supported_channel.startswith(channel):
            return supported_channel

    raise ValueError("unsupported channel: {} (supported: {})".format(
        channel, ", ".join(supported_channel)))


def _validate_city(city):

    city = city.strip().title()
    supported_cities = \
        ("Adelaide", "Brisbane", "Canberra", "Melbourne", "Sydney")

    for supported_city in supported_cities:
        if supported_city.startswith(city):
            return supported_city

    raise ValueError("unsupported city: {} (supported cities are: {})"\
        .format(city, ", ".join(supported_cities)))

