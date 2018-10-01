[![Build Status](https://travis-ci.org/andycasey/get-rich-or-die-trying.svg?branch=master)](https://travis-ci.org/andycasey/get-rich-or-die-trying)
[![Docs](https://readthedocs.org/projects/get-rich-or-die-tryin/badge/?version=latest)](http://get-rich-or-die-tryin.readthedocs.io/en/latest/)

# Get Rich or Die Tryin'

Don't ask.

## Domain API client example

````python
from domain import DomainClient

domain = DomainClient()

# Search for properties.
results = domain.properties("Mockingbird lane")

print(results[0])
>>> {u'id': u'PB-5682-MC',
 u'relativeScore': 100,
 u'addressComponents': {u'streetTypeLong': u'Road',
 u'streetType': u'Rd',
 u'suburb': u'Pheasants Nest',
 u'state': u'NSW',
 u'unitNumber': u'',
 u'postcode': u'2574',
 u'streetNumber': u'145',
 u'streetName': u'Mockingbird'},
 u'address': u'145 Mockingbird Road, Pheasants Nest NSW 2574'}


# General sales metadata
print(domain.sales_results_metadata)
>>> {u'auctionedDate': u'2017-08-12',
 u'lastModifiedDateTime': u'2017-08-12T08:45:37.576Z'}


# Check recent sales results in the best city ever
print(domain.sales_results("melb"))
>>> {u'adjClearanceRate': 0.717219589257504,
 u'median': 898000,
 u'numberAuctioned': 623,
 u'numberListedForAuction': 823,
 u'numberSold': 454,
 u'numberUnreported': 8,
 u'numberWithdrawn': 10,
 u'totalSales': 412839650.0}
 ````


## CoreLogic API
