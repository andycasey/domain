

from collections import OrderedDict

package_plan_scopes = OrderedDict([
    ("AgentsAndListingsInnovationPlan", (
        "api_agencies_read",
        "api_listings_read"
    )),
    ("PropertyAndLocationInnovationPlan", (
        "api_properties_read",
        "api_salesresults_read"
    )),
    ("AgentsAndListingsBusinessPlan", (
        "api_agencies_read",
        "api_listings_read",
        "api_propertyreports_read"
    )),
    ("PropertyAndLocationBusinessPlan", (
        "api_properties_read",
        "api_salesresults_read",
        "api_propertyreports_read",
        "api_suburbperformance_read"
    )),
])

