

from . import (base, validate, utils)

__all__ = ["DomainClient"]

class DomainClient(base.BaseDomainClient):

    _API_VERSION = "v1"
    _API_HOST = "api.domain.com.au"
    _API_SCHEMES = ["http", "https"]

    @requires_scope("api_addresslocators_read")
    def address_locators(self, search_level, unit_number=None, 
                         street_number=None, street_name=None, street_type=None, 
                         suburb=None, state=None, postcode=None, **kwargs):
        r"""
        Retrieves matching ids for use in other services.

        Use this endpoint to retrieve IDs that may be used to query information 
        from other endpoints. For example use `id` of the `Suburb` level to 
        query [`demographics`](/docs/endpoints/demographics/demographics_get).
        
        :param search_level: 
            Requested search level. Valid values are: `Address`, and `Suburb`.
        
        :param unit_number: [optional]
            Unit number.
        
        :param street_number: [optional]
            Street number.
        
        :param street_name: [optional]
            Street name.
        
        :param street_type: [optional]
            Street type.
        
        :param suburb: [optional]
            Suburb.
        
        :param state: [optional]
            State.
        
        :param postcode: [optional]
            Postcode.
        """

        search_level = validate.case_insensitive_string(search_level,
                                                        ("Address", "Suburb"))

        data = dict(search_level=search_level, unit_number=unit_number, 
                    street_number=street_number, street_name=street_name, 
                    street_type=street_type, suburb=suburb, state=state, 
                    postcode=postcode)

        return self._api_request(f"addressLocators", data, **kwargs)
    

    @requires_scope("api_agencies_read")
    def agencies(self, id, **kwargs):
        r"""
        Retrieves a specific agency details.
        
        :param id: 
            Agency identifier.
        """
        return self._api_request(f"agencies/{id}", **kwargs)
    

    @requires_scope("api_listings_read")
    def agencies_listings(self, id, listingStatusFilter=None, 
                          date_updated_since=None, page_number=None, 
                          page_size=None, **kwargs):
        r"""
        Retrieves listings across all channels for a specific agency matching 
        specified criteria.

        Note that the result page size is clamped at 200. Requesting a page 
        size greater than this will be treated as if only a page size of 200 
        were requested.

        :param id: 
            Agency identifier.
        
        :param listingStatusFilter: [optional]
            Filter for listing status. Valid values are: `live`, and 
            `liveAndArchived`.
        
        :param date_updated_since: [optional]
            Filter to remove listings not updated since before the given date 
            time.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """

        # TODO: Revisit listingStatusFilter, which is also referred to elsewhere
        #       as includedArchivedListings.

        listingStatusFilter = validate.case_insensitive_string(
            listingStatusFilter, ("live", "liveAndArchived"))

        data = dict(listingStatusFilter=listingStatusFilter, 
                    date_updated_since=date_updated_since, 
                    page_number=page_number, page_size=page_size)
        return self._api_request(f"agencies/{id}/listings", data, **kwargs)
    

    @requires_scope("api_agencies_read")
    def agencies_statistics(self, id, **kwargs):
        r"""
        Retrieves statistics across all channels for a specific agency.
        
        :param id: 
            Agency identifier.
        """
        return self._api_request(f"agencies/{id}/statistics", **kwargs)
    

    @requires_scope("api_agencies_read")
    def agencies_subscriptions(self, id, channel=None, **kwargs):
        r"""
        Retrieves the active subscriptions for the specific agency.

        :param id: 
            Agency identifier.
        
        :param channel: [optional]
            Channel. Either `residential` or `commercial` (case insensitive). 
            Defaults to `residential` if not provided.
        """
        channel = validate.case_insensitive_string(channel,
                                                   ("residential", "commercial"),
                                                   default="residential")

        data = dict(channel=channel)
        return self._api_request(f"agencies/{id}/subscriptions", data, **kwargs)
    

    @requires_scope("api_agencies_read")
    def agencies_bundlecontracts(self, id, **kwargs):
        r"""
        Retrieves the product bundle contracts applicable to the specific agency.
        
        :param id: 
            Agency identifier.
        """
        return self._api_request(f"agencies/{id}/bundlecontracts", **kwargs)
    

    @requires_scope("api_agencies_read")
    def agencies(self, query, page_number=None, page_size=None, **kwargs):
        r"""
        Retrieves summary of agencies matching the specified criteria.
        
        :param query: 
            Search phrase.  e.g. name:"Agency XYZ".
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """

        data = dict(query=query, page_number=page_number, page_size=page_size)
        return self._api_request(f"agencies", data, **kwargs)
    

    @requires_scope("api_agencies_read")
    def agents_search(self, query, page_number=None, page_size=None, **kwargs):
        r"""
        Search for agents by name.

        The returned Agent ID can be used to get an agent details by ID. 
        See `GET /agents/{id}/`
        
        :param query: 
            The name, or portion of name, to search for.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results (maximum 20).
        """

        # TODO: Some reason the page_size here is max to 20, but not elsewhere?
        # TODO: method parameters: `query` vs `q`

        data = dict(query=query, page_number=page_number, page_size=page_size)
        return self._api_request(f"agents/search", data, **kwargs)
    

    @requires_scope("api_agencies_read")
    def agents(self, id, **kwargs):
        r"""
        Retrieves a specific agent details, including contact information.

        :param id: 
            Agent identifier.
        """
        return self._api_request(f"agents/{id}", **kwargs)
    

    @requires_scope("api_listings_read")
    def agents_listings(self, id, date_updated_since=None, 
                        includedArchivedListings=None, page_number=None, 
                        page_size=None, **kwargs):
        r"""
        Gets listing using an Agents id.
        
        :param id: 
            Agent identifier.
        
        :param date_updated_since: [optional]
            Filter to remove listings not updated since before the given date 
            time.
        
        :param includedArchivedListings: [optional]
            Filter to remove listings that have been archived.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """

        data = dict(date_updated_since=date_updated_since, 
                    includedArchivedListings=includedArchivedListings, 
                    page_number=page_number, page_size=page_size)
        return self._api_request(f"agents/{id}/listings", data, **kwargs)
    

    @requires_scope("api_demographics_read")
    def demographics(self, level, id, types=None, year=None, **kwargs):
        r"""
        Retrieves demographic information.
        
        :param level: 
            Geographic level. Valid values are: `Postcode`, `Suburb`.
        
        :param id: 
            Location identifier. If the geographic level is Suburb this is a 
            Suburb ID value, if the geographic level is postcode this is a 
            Postcode ID value.  See the `/addressLocators` endpoint.
        
        :param types: [optional]
            Comma separated list of demographic data requested. If not provided,
            all data will be returned. Valid values are: 
                `AgeGroupOfPopulation`, 
                `CountryOfBirth`,
                `NatureOfOccupancy`,
                `GeographicalPopulation`,
                `DwellingStructure`,
                `HousingLoanRepayment`,
                `MaritalStatus`,
                `Religion`,
                `Occupation`,
                `EducationAttendance`,
                `TransportToWork`.
        
        :param year: [optional]
            Year of the source data.
        """

        # TODO: year docs say Valid values are: `2011`, `2016`.

        level = validate.case_insensitive_string(level, ("Postcode", "Suburb"))

        if types is not None:
            available = [
                "AgeGroupOfPopulation", 
                "CountryOfBirth",
                "NatureOfOccupancy",
                "GeographicalPopulation",
                "DwellingStructure",
                "HousingLoanRepayment",
                "MaritalStatus",
                "Religion",
                "Occupation",
                "EducationAttendance",
                "TransportToWork"
            ]
            types = [validate.case_insensitive_string(_, available) for _ in types]

        data = dict(level=level, id=id, types=types, year=year)
        return self._api_request(f"demographics", data, **kwargs)
    

    @requires_scope("api_properties_read")
    def disclaimers(self, ids=None, **kwargs):
        r"""
        Retrieves disclaimers for given ids.

        :param ids: [optional]
            Comma separated list of ids. Eg. "1,2,3".
        """

        # TODO: What kind of disclaimers?! What if we give None.
        data = dict(ids=ids)
        return self._api_request(f"disclaimers", data, **kwargs)
    

    @requires_scope("api_properties_read")
    def disclaimers_product(self, product, **kwargs):
        r"""
        Retrieves disclaimers for given product.

        :param product: 
            Possible product values: `PropertyData`, `AURIN`, `HomePriceGuide`.
        """

        product = validate.case_insensitive_string(
            product, ("PropertyData", "AURIN", "HomePriceGuide"))

        return self._api_request(f"disclaimers/product/{product}", **kwargs)
    

    @requires_scope("api_enquiries_read", "api_enquiries_write")
    def enquiries(self, id, **kwargs):
        r"""
        Retrieves a specific enquiry.
        
        :param id: 
            Enquiry identifier.
        """
        return self._api_request(f"enquiries/{id}", **kwargs)
    

    @requires_scope("api_enquiries_read", "api_enquiries_write")
    def enquiries(self, agency_id=None, agent_id=None, date_from=None, 
                  date_to=None, page_number=None, **kwargs):
        r"""
        Searches enquiries based on agents or agencies.
        
        :param agency_id: [optional]
            Agency identifier.
        
        :param agent_id: [optional]
            Agent identifier.
        
        :param date_from: [optional]
            Enquiries received date_from.
        
        :param date_to: [optional]
            Enquiries received up date_to.
        
        :param page_number: [optional]
            Page number for paginated results (25 per page).
        """
        # TODO: why is there no page_size here?!
        # TODO: Why is page_number max 25 here but not everywhere?
        data = dict(agency_id=agency_id, agent_id=agent_id, 
                    date_from=date_from, date_to=date_to, 
                    page_number=page_number)
        return self._api_request(f"enquiries", data, **kwargs)
    

    @requires_scope("api_listings_read", "api_listings_write")
    def listings(self, id, **kwargs):
        r"""
        Retrieves a specific listing.
        
        :param id: 
            Listing identifier.
        """
        return self._api_request(f"listings/{id}", **kwargs)
    

    @requires_scope("api_enquiries_read", "api_enquiries_write")
    def listings_enquiries(self, id, page_number=None, **kwargs):
        r"""
        Returns enquiries for a given listing.

        :param id: 
            Listing identifier.
        
        :param page_number: [optional]
            Page number for paginated results (25 per page).
        """
        # TODO: Why is page_number max 25 here but not everywhere?

        data = dict(page_number=page_number)
        return self._api_request(f"listings/{id}/enquiries", data, **kwargs)
    

    @requires_scope("api_listings_read")
    def listings_statistics(self, id, time_period=None, **kwargs):
        r"""
        Retrieves listings stats for the specified listing.

        :param id: 
            Listing identifier.
        
        :param time_period: [optional]
            The time period to show statistics for. Valid values are: 
            `last7Days`, `last90Days`, `wholeCampaign`.
        """

        time_period = validate.case_insensitive_string(
            time_period, ("last7Days", "last90Days", "wholeCampaign"))

        data = dict(time_period=time_period)
        return self._api_request(f"listings/{id}/statistics", data, **kwargs)
    

    @requires_scope("api_listings_read")
    def listings_statistics(self, agent_id, time_period, status_filter, 
                            page_number=None, page_size=None, **kwargs):
        r"""
        Retrieves stats for the listings of a given agent.
        
        :param agent_id: 
            Agent identifier.
        
        :param time_period: 
            The time period to show statistics for. Valid values are: 
            `last7Days`, `last90Days`, `wholeCampaign`.
        
        :param status_filter: 
            Listing filter.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """

        # TODO: Is statusFilter the same as listingStatusFilter elsewhere?

        time_period = validate.case_insensitive_string(
            time_period, ("last7Days", "last90Days", "wholeCampaign"))

        data = dict(agent_id=agent_id, 
                    time_period=time_period, status_filter=status_filter,
                    page_number=page_number, page_size=page_size)
        return self._api_request(f"listings/statistics", data, **kwargs)
    

    @requires_scope("api_listings_read")
    def listings_processingreports(self, agency_id, provider_ad_id, **kwargs):
        r"""
        Searches processing reports.
        
        :param agency_id: 
            Domain agency Id.
        
        :param provider_ad_id: 
            External provider advertisement identifier.
        """
        data = dict(agency_id=agency_id, provider_ad_id=provider_ad_id)
        return self._api_request(f"listings/processingReports", data, **kwargs)
    

    @requires_scope("api_listings_read")
    def listings_processingreports(self, id, **kwargs):
        r"""
        Gets the processing report.

        :param id: 
            Report id.
        """
        # TODO: consider method name.
        return self._api_request(f"listings/processingReports/{id}", **kwargs)
    

    @requires_scope("api_listings_read", "api_listings_write")
    def listings_locations(self, terms=None, **kwargs):
        r"""
        Suggests listing locations.

        The resulting suggested location can be of type "suburb", "area", or
        "region". 

        The `name` property corresponds to the type of location returned.

        The area name / region name can be fed into the corresponding fields 
        search fields.  See [`v1/listings/residential/_search`](/docs/endpoints/listings/listings_detailedresidentialsearch)

        :param terms: [optional]
            Suburb / area / region prefix, or postcode.
        """
        # TODO: the docstring and documentation for this method is not clear.
        data = dict(terms=terms)
        return self._api_request(f"listings/locations", data, **kwargs)
    

    @property
    @requires_scope("api_agencies_read")
    def me_agencies(self):
        r"""
        Retrieves summary agency information associated to the current user.
        """

        # TODO: rename to my_agencies??
        return self._api_request(f"me/agencies")
    

    @requires_scope("api_listings_read", "api_listings_write")
    def projects(self, id, **kwargs):
        r"""
        Retrieves a specific project.

        :param id: 
            Project identifier.
        """
        return self._api_request(f"projects/{id}", **kwargs)
    

    @requires_scope("api_listings_read", "api_listings_write")
    def projects_listings(self, id, **kwargs):
        r"""
        Retrieves listings of a project.

        :param id: 
            Project identifier.
        """
        # TODO: there was no description here for the param ID in swagger
        return self._api_request(f"projects/{id}/listings", **kwargs)
    

    @requires_scope("api_listings_read", "api_listings_write")
    def projects(self, agency_id=None, page_number=None, page_size=None, 
                 **kwargs):
        r"""
        Searches projects.

        Note that the result page size is clamped at 100.  Requesting a page 
        size greater than this will be treated as if only a page size of 100 
        were requested.
        
        :param agency_id: [optional]
            Restricts to the provided agency.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """
        data = dict(agency_id=agency_id, 
                    page_number=page_number, page_size=page_size)
        return self._api_request(f"projects", data, **kwargs)
    

    @requires_scope("api_properties_read")
    def properties(self, id, **kwargs):
        r"""
        Retrieves a specific property.

        Applicable [policies](/docs/support/policies) apply here include APM 
        attribution and appropriate state government attribution.

        :param id: 
            Property identifier. Use the `_suggest` resource to determine the 
            propertyId.
        """
        # TODO: propertyID should be `property_id` and reference `_suggest`
        #       better.
        return self._api_request(f"properties/{id}", **kwargs)
    

    @requires_scope("api_properties_read")
    def properties_priceestimate(self, id, **kwargs):
        r"""
        Retrieves the current price estimate for the given property.

        The price estimate data is refreshed monthly, typically towards the end
        of each month. The price estimate provides a guide of the approximate 
        market value for a property.

        :param id: 
            Property identifier.  Use the `_suggest` resource to determine the 
            propertyId.
        """
        # TODO: propertyID should be `property_id` and reference `_suggest`
        #       better.
        return self._api_request(f"properties/{id}/priceEstimate", **kwargs)
    

    @requires_scope("api_properties_read")
    def properties_suggest(self, terms, channel="All", page_size=None, **kwargs):
        r"""
        Provides property suggestions.

        Applicable [policies](/docs/support/policies) apply here include APM 
        attribution.

        :param terms: 
            Terms on which to base suggestions.
                
        :param channel: [optional]
            Restrict the suggestions to this type of property: `All` (default), 
            `Residential`, `Commercial`.

        :param page_size: [optional]
            Number of suggestions (maximum 20).
        """
        # TODO: In Swagger docs the page_size was given before channel, which
        #       probably isn't right.

        channel = validate.case_insensitive_string(
            channel, ("All", "Residential", "Commercial"))
        data = dict(terms=terms, page_size=page_size, channel=channel)
        return self._api_request(f"properties/_suggest", data, **kwargs)
    

    @requires_scope("api_propertyreports_read")
    def property_reports(self, property_type, street_number, street_name, 
                         suburb, state, unit_number=None, street_type=None, 
                         postcode=None, area_size=None, bedrooms=None, 
                         bathrooms=None, parking=None, prepared_for=None, 
                         product_code=None, **kwargs):
        r"""
        Retrieves a property report based on query parameters.

        :param property_type: 
            Type of property. Valid options are: `House`, `Unit`.
        
        :param street_number: 
            Street number.
        
        :param street_name: 
            Street name.
        
        :param suburb: 
            Suburb e.g. `Pyrmont`.
        
        :param state: 
            State e.g. `NSW`.
        
        :param unit_number: [optional]
            Unit number.
        
        :param street_type: [optional]
            Street type e.g. `Pl`.
        
        :param postcode: [optional]
            Postcode e.g. `2009`.
        
        :param area_size: [optional]
            Area size.
        
        :param bedrooms: [optional]
            Number of bedrooms.
        
        :param bathrooms: [optional]
            Number of bathrooms.
        
        :param parking: [optional]
            Number of parking spots.
        
        :param prepared_for: [optional]
            "Prepared for" information.
        
        :param product_code: [optional]
            Report product code.
        """

        # TODO: Validations!
        # TODO: Product code??!
        # TODO: prepared for??!

        property_type = validate.case_insensitive_string(property_type,
                                                         ("House", "Unit"))

        data = dict(property_type=property_type, street_number=street_number, 
                    street_name=street_name, suburb=suburb, state=state, 
                    unit_number=unit_number, street_type=street_type, 
                    postcode=postcode, area_size=area_size, 
                    bedrooms=bedrooms, bathrooms=bathrooms, parking=parking, 
                    prepared_for=prepared_for, product_code=product_code)

        return self._api_request(f"propertyReports", data, **kwargs)
    

    @requires_scope("api_salesresults_read")
    def sales_results_metadata(self, **kwargs):
        r""" Retrieves metadata regarding sales result data. """
        return self._api_request(f"salesResults/_head", **kwargs)
    

    @requires_scope("api_salesresults_read")
    def sales_results(self, city, **kwargs):
        r"""
        Retrieves sales results for a given city.

        :param city: 
            City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, 
            `Adelaide`, `Canberra`.
        """
        city = validate.city(city)
        return self._api_request(f"salesResults/{city}", **kwargs)
    

    @requires_scope("api_salesresults_read")
    def sales_results_listings(self, city, **kwargs):
        r"""
        Retrieves listing summaries corresponding to the sales results.
        
        :param city: 
            City. Supported cities are: `Sydney`, `Melbourne`, `Brisbane`, 
            `Adelaide`, `Canberra`.
    
        """
        city = validate.city(city)
        return self._api_request(f"salesResults/{city}/listings", **kwargs)
    

    @requires_scope("api_locations_read")
    def locations_schools(self, id, **kwargs):
        r"""
        Retrieves a specific school.
        
        :param id: 
            School identifier.
        """
        return self._api_request(f"locations/schools/{id}", **kwargs)
    

    @requires_scope("api_locations_read")
    def locations_schools(self, coordinate=None, **kwargs):
        r"""
        Searches schools based on specified criteria.
        
        :param coordinate: [optional]
            Filter schools to include the specified coordinate in their 
            catchment area (latitude, longitude).
        """
        # TODO: Update docs with better specifications of coordinates.
        data = dict(coordinate=coordinate)
        return self._api_request(f"locations/schools", data, **kwargs)
    

    @requires_scope("api_webhooks_write")
    def subscriptions(self, id, **kwargs):
        r"""
        Retrieves a webhook subscription.
        
        :param id: 
            Subscription identifier.
        """
        return self._api_request(f"subscriptions/{id}", **kwargs)
    

    @requires_scope("api_suburbperformance_read")
    def suburb_performance_statistics(self, state, suburb_id, property_category,
        chronological_span, tPlusFrom, tPlusTo, bedrooms=None, values=None, 
        **kwargs):
        r"""
        Retrieves suburb performance data.

        :param state: 
            State where the suburb is.
        
        :param suburb_id: 
            Suburb Identifier.  Use the `addressLocators` resource to determine 
            the `suburb_id`.
        
        :param property_category: 
            Property Category. Valid values are: `house`, `unit`, `land`.
        
        :param chronological_span: 
            The size of each chunk of information we want in months. 3, 6, or 12.
        
        :param tPlusFrom: 
            Countdown number in chronological spans from the current (current 
            chronological span is 1).
        
        :param tPlusTo: 
            Countdown number in chronological spans from the current (current 
            chronological span is 1, 2 chronological spans ago is 3).
        
        :param bedrooms: [optional]
            Restrict statistics to properties with this number of bedrooms.
        
        :param values: [optional]
            Values to be returned for the series.  If the field is not provided, 
            all available values for the SeriesInfo will be returned. You can 
            specify multiple values using comma separated text. Valid values 
            are: 

            - `MedianSoldPrice`
            - `AuctionNumberAuctioned`
            - `AuctionNumberSold`
            - `AuctionNumberWithdrawn`
            - `NumberSold`
            - `LowestSoldPrice`
            - `HighestSoldPrice`
            - `5thPercentileSoldPrice`
            - `25thPercentileSoldPrice`
            - `75thPercentileSoldPrice`
            - `95thPercentileSoldPrice`
            - `DaysOnMarket`
            - `DiscountPercentage`
            - `MedianRentListingPrice`
            - `NumberRentListing`
            - `HighestRentListingPrice`
            - `LowestRentListingPrice`
            - `MedianSaleListingPrice`
            - `NumberSaleListing`
            - `HighestSaleListingPrice`
            - `LowestSaleListingPrice`
        """

        # tplusfrom/tplusto/chronologicalSpan is all fucked up.
        # validation for values.

        property_category = validate.case_insensitive_string(
            property_category, ("house", "unit", "land"))

        data = dict(state=state, suburb_id=suburb_id, 
                       property_category=property_category, 
                       chronological_span=chronological_span, 
                       tPlusFrom=tPlusFrom, tPlusTo=tPlusTo, 
                       bedrooms=bedrooms, values=values)
        return self._api_request(f"suburbPerformanceStatistics", data, **kwargs)
    

    @requires_scope("api_webhooks_write")
    def webhooks_subscriptions(self, id, page_number=None, page_size=None, 
                               **kwargs):
        r"""
        Retreives all webhook subscriptions.

        :param id: 
            Webhook identifier.
        
        :param page_number: [optional]
            Page number for paginated results.
        
        :param page_size: [optional]
            Page size for paginated results.
        """
        # TODO: Swagger has no docs for page_number or page_size.
        data = dict(page_number=page_number, page_size=page_size)
        return self._api_request(f"webhooks/{id}/subscriptions", data, **kwargs)
    