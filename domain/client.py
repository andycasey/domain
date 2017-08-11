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




def _validate_city(city):

    city = city.strip().title()
    supported_cities = \
        ("Adelaide", "Brisbane", "Canberra", "Melbourne", "Sydney")

    for supported_city in supported_cities:
        if supported_city.startswith(city):
            return supported_city

    raise ValueError("unsupported city: {} (supported cities are: {})"\
        .format(city, ", ".join(supported_cities)))

