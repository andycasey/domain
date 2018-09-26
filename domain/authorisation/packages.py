

scopes = dict([
    ("CRM", ()),

])

throttle_rates = dict([
    ("CRM", 2),
])

{'api_addresslocators_read',
 'api_agencies_read',
 'api_demographics_read',
 'api_enquiries_read',
 'api_enquiries_write',
 'api_listings_read',
 'api_listings_write',
 'api_locations_read',
 'api_properties_read',
 'api_propertyreports_read',
 'api_salesresults_read',
 'api_suburbperformance_read',
 'api_webhooks_write'}



 # Only CRM has access to v1/enquiries/

 # Only Properties + Locations (Business) has access to /properties/{id}/priceEstimate

 # Properties + Locations (Innovation) has access to v1/properties/{id}
 #                                     but not /properties/{id}/priceEstimate

# Only Agents + Listings (Business) has access to  v1/agencies/{id}/statistics
# Agents + Listings (Innovation) has access to v1/listings/locations,
#                                           but not v1/agencies/{id}/statistics

