[![Build Status](https://travis-ci.org/andycasey/domain.svg?branch=master)](https://travis-ci.org/andycasey/domain)
[![Docs](https://readthedocs.org/projects/domain/badge/?version=latest)](http://domain.readthedocs.io/en/latest/)

# Python client for the Domain property API 

It does what it says on the tin.

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


# Authentication 

You will first need to [sign up for a Domain developer account](https://developer.domain.com.au/).
Then you will be able to [create a project](https://developer.domain.com.au/projects).

Now you will need to create some credentials. I suggest to create an OAuth 2.0 Client. To do this correctly you will be given a Client ID and Client Secret. Copy those down; you'll need these later.

### Note
The Domain API has changed since this code was written. That means some of the way this code works to find out which credentials are required for a given API end point, are no longer needed. This README just tells you what you need to do to make everything work. In practice, the abstraction of plan <-> scope needs to be updated to reflect the new API end points.


Next you'll need to add API Access to your project. Sign up for everything that is free, and then create a credentials file (called `client_credentials.yaml`) in the following format:
 
````yaml
- client_id: <CLIENT_ID>
  client_secret: <CLIENT_SECRET>
  package_and_plan: AgentsAndListingsInnovationPlan 
- client_id: <CLIENT_ID>
  client_secret: <CLIENT_SECRET>
  package_and_plan: PropertyAndLocationInnovationPlan
````


Now you can use those credentials (or any number of Client ID/Client Secret pairs)
to authenticate and use the API from Python:

````python
from domain.client import DomainClient

dc = DomainClient("client_credentials.yaml")
````

That's it! 

The `DomainClient` will work out which scope is required for each API
end point, and will create authentication tokens (Oauth2) as needed. New tokens
will be generated when the old ones expire, and the token handling
(`domain.authorisations.token.Token`) will automatically throttle your requests
so that you your queries don't fail due to the Domain API rate limits.

You can override this behaviour by supplying your own `token=Token` keyword 
argument to any API method in the `DomainClient` class.


# API Example Usage

````python
# Suggest properties based on search terms
results = dc.properties_suggest("Mockingbird lane")

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
print(dc.sales_results_metadata())
>>> {u'auctionedDate': u'2017-08-12',
 u'lastModifiedDateTime': u'2017-08-12T08:45:37.576Z'}


# Check recent sales results in the best city ever.
print(dc.sales_results("Melbourne"))
>>> {u'adjClearanceRate': 0.717219589257504,
 u'median': 898000,
 u'numberAuctioned': 623,
 u'numberListedForAuction': 823,
 u'numberSold': 454,
 u'numberUnreported': 8,
 u'numberWithdrawn': 10,
 u'totalSales': 412839650.0}
 ````
