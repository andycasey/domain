# -*- coding: utf-8 -*-

from . import validate, utils
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


    def residential_listings(self, listing_type=None, property_types=None,
        property_features=None, listing_attributes=None, bedrooms=None,
        bathrooms=None, car_spaces=None, price_range=None, land_area_range=None,
        locations=None, location_terms=None, keywords=None, inspections=None, 
        auction=None, sort_by=None, sort_ascending=True, page=None, 
        page_size=None, **kwargs):
        r"""
        Retrieves residential listings matching the specified criteria. Search
        results are limited to the first 1000 results (by the Domain API).

        If the number of results is greater, the intention is to refine the 
        search by adding more restrictive parameters, to find a relevant set of 
        results.
        """

        listing_type = validate.listing_type(listing_type)
        property_types = validate.property_types(property_types)
        listing_attributes = validate.listing_attributes(listing_attributes)

        min_bedrooms, max_bedrooms = validate.integer_range(bedrooms)
        min_bathrooms, max_bathrooms = validate.integer_range(bathrooms)
        min_car_spaces, max_car_spaces = validate.integer_range(car_spaces, "")
        min_price, max_price = validate.integer_range(price_range, "")
        min_land_area, max_land_area = validate.integer_range(land_area_range, "")

        #advertiser_ids = validate.advertiser_ids(advertiser_ids)

        locations = [dict(state="VIC", suburb="Richmond", postCode="3121",
            includeSurroundingSuburbs=False)]


        # locations
        #location_tmers
        # keywords
        # inspections
        # auction
        # sort_by
        # sort_ascending
        # page
        # page_size


        data = dict(
            listingType=listing_type,
            propertyTypes=property_types,
            listingAttributes=listing_attributes,
            minBedrooms=min_bedrooms,
            maxBedrooms=max_bedrooms,
            minBathrooms=min_bathrooms,
            maxBathrooms=max_bathrooms,
            minCarspaces=min_car_spaces,
            maxCarspaces=max_car_spaces,
            minPrice=min_price,
            maxPrice=max_price,
            minLandArea=min_land_area,
            maxLandArea=max_land_area,
            #advertiserIds=advertiser_ids,
            locations=locations
            )
        return self._post_api_request("listings/residential/_search", data=data)




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