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


## Authenticating 

You will first need to [sign up for a Domain developer account](https://developer.domain.com.au/).
Then you will be able to [create an application](https://developer.domain.com.au/applications) and get a Client ID and Client Secret. 
These will be used for authentication.

Note that the Domain API has multiple Packages and Plans that give access to
different end points of their API. You can sign up for the 
"Agents and Listings - Innovation Plan" and the
"Property and Location - Innovation Plan" for free.
Each package/plan combination will grant you a different Client ID and Client
Secret, which can make it a little difficult to know when to use which one.
Thankfully, this Python client takes care of all of that for you. 

Enter your credentials into a file (e.g. called client_credentials.yaml) in the
following format:

````yaml
- client_id: <AGENTS_AND_LISTINGS_ID>
  client_secret: <AGENTS_AND_LISTINGS_SECRET>
  package_and_plan: AgentsAndListingsInnovationPlan 
- client_id: <PROPERTY_AND_INNOVATION_ID>
  client_secret: <PROPERTY_AND_INNOVATION_SECRET>
  package_and_plan: PropertyAndLocationInnovationPlan
````


Now you can use those credentials (or any number of Client ID/Client Secret pairs)
to authenticate and use the API from Python:

````python
from domain import DomainClient

dc = DomainClient("client_credentials.yaml")
````

## API Example.


````python
# Suggest properties based on search terms
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


# General sales metadata.
print(domain.sales_results_metadata())
>>> {u'auctionedDate': u'2017-08-12',
 u'lastModifiedDateTime': u'2017-08-12T08:45:37.576Z'}


# Check recent sales results in the best city ever.
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
