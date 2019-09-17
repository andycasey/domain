import sys
import yaml

from domain.client import DomainClient


if __name__ == "__main__":

    dc = DomainClient("client_credentials.yaml")

    # TODO: Check if it's a listing ID or URL
    address_parts = sys.argv[1:]
    if len(address_parts) == 1:
        try:
            recent_listing_id = int(address_parts[0])
        except:
            # URL
            None

    else:            

        input_address = " ".join(sys.argv[1:])

        properties_suggest = dc.properties_suggest(input_address)

        if properties_suggest[0]["relativeScore"] < 100:
            raise a

        property_ = dc.properties(properties_suggest[0]["id"])

        # Get most recent listing.
        try:
            recent_listing_id = sorted(set([ph["advertId"] for ph in property_.get("photos", [])]))[-1]

        except IndexError:
            raise ValueError(f"no property listings found for {property_['address']}")


    # Get sold details.
    listing = dc.listings(recent_listing_id)

    details = dict(addressParts=listing["addressParts"],
                   saleDetails=listing["saleDetails"])

    print(yaml.dump(details, sort_keys=True, indent=2))
