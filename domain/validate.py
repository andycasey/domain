# -*- coding: utf-8 -*-


def case_insensitive_string(string, available, default=None):

    if string is None:
        return default

    _available = [each.lower() for each in available]

    try:
        index = _available.index(f"{string}".lower())

    except ValueError:
        raise ValueError(f"unrecognised input ('{string}') - must be in {available}")

    else:
        return available[index]



def listing_type(entry):
    if entry is None:
        return ""

    available_listing_types = ["Sale", "Rent", "Share", "Sold", "NewHomes"]
    _alt = [each.lower() for each in available_listing_types]

    try:
        index = _alt.index(str(entry).lower())

    except ValueError:
        raise ValueError("listing type must be one of: {}".format(
            ", ".join(available_listing_types)))

    else:
        return available_listing_types[index]



def property_types(entries):

    if entries is None: 
        return [""]

    available_property_types = [
        "AcreageSemiRural", "ApartmentUnitFlat",  "BlockOfUnits", "CarSpace", 
        "DevelopmentSite", "Duplex", "Farm", "NewHomeDesigns", "House", 
        "NewHouseLand", "NewLand", "NewApartments", "Penthouse", 
        "RetirementVillage", "Rural", "SemiDetached", "SpecialistFarm", 
        "Studio", "Terrace", "Townhouse", "VacantLand", "Villa"]
    _lower_pt = [each.lower() for each in available_property_types]

    if isinstance(entries, (str, unicode)):
        entries = [entries]

    validated_entries = []
    for entry in entries:
        try:
            index = _lower_pt.index(str(entry).lower())

        except IndexError:
            raise ValueError(
                "Unrecognised property type '{}'. Available types: {}".format(
                    entry, ", ".join(available_property_types)))

        validated_entries.append(available_property_types[index])

    return validated_entries



def listing_attributes(entries):
    if entries is None:
        return [""]

    available_listing_attributes = ["HasPhotos", "HasPrice", "NotUpForAuction",
        "NotUnderContract", "MarkedAsNew"]
    _lower_la = [each.lower() for each in available_listing_attributes]

    if isinstance(entries, (str, unicode)):
        entries = [entries]

    validated_entries = []
    for entry in entries:
        try:
            index = _lower_la.index(str(entry).lower())

        except IndexError:
            raise ValueError(
                "Unrecognised listing attribute {}. Available attributes: {}"\
                .format(entry, ", ".join(available_listing_attributes)))

        validated_entries.append(available_listing_attributes[index])

    return validated_entries


def integer_range(entry, default_value=-1):

    entry = entry or default_value

    # Allow a single value to be given.
    if isinstance(entry, int) or entry == default_value:
        return (entry, entry)

    if len(entry) > 2:
        raise ValueError("only lower and upper range can be given, not a list")

    return tuple(sorted(entry))


def city(string, **kwargs):
    cities = ("Sydney", "Melbourne", "Brisbane", "Adelaide", "Canberra")
    return case_insensitive_string(string, cities, **kwargs)


def advertiser_ids(entries):

    if entries is None:
        return [""]

    if isinstance(entries, (str, unicode)):
        entries = [entries]

    return entries

