[![Build Status](https://travis-ci.org/andycasey/domain.svg?branch=master)](https://travis-ci.org/andycasey/domaing)
[![Docs](https://readthedocs.org/projects/domain/badge/?version=latest)](http://domain.readthedocs.io/en/latest/)

# Python client for the Domain property API 


# Installation

Using ``pip``:

````bash
pip install domain
````

Or installing from source:

````bash
git clone git@github.com:andycasey/domain.git
cd domain/
python setup.py install
````


## Example 

````python
from domain import DomainClient

domain = DomainClient()

# Search for properties.
results = domain.properties_suggest("Mockingbird lane")

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
print(domain.sales_results_metadata())
>>> {u'auctionedDate': u'2017-08-12',
 u'lastModifiedDateTime': u'2017-08-12T08:45:37.576Z'}


# Check recent sales results in the best city ever
print(domain.sales_results("Melbourne"))
>>> {u'adjClearanceRate': 0.717219589257504,
 u'median': 898000,
 u'numberAuctioned': 623,
 u'numberListedForAuction': 823,
 u'numberSold': 454,
 u'numberUnreported': 8,
 u'numberWithdrawn': 10,
 u'totalSales': 412839650.0}
 ````
