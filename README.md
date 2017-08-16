[![Build Status](https://travis-ci.org/andycasey/get-rich-or-die-trying.svg?branch=master)](https://travis-ci.org/andycasey/get-rich-or-die-trying)

# Get Rich or Die Tryin'

Don't ask.

# API client example

````python
from domain.client import DomainClient

domain = DomainClient()

# Search for properties.
results = domain.properties("Mockingbird lane")

print(results[0])
>>> {u'id': u'PB-5682-MC', u'relativeScore': 100, u'addressComponents': {u'streetTypeLong': u'Road', u'streetType': u'Rd', u'suburb': u'Pheasants Nest', u'state': u'NSW', u'unitNumber': u'', u'postcode': u'2574', u'streetNumber': u'145', u'streetName': u'Mockingbird'}, u'address': u'145 Mockingbird Road, Pheasants Nest NSW 2574'}

````