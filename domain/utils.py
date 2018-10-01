
""" General utilities. """

__all__ = ["validate_channel", "validate_city", "uri"]


def uri(end_point, host, version, scheme):
    r"""
    Return the unique resource identifier for the requested end point, host,
    version, and scheme.
    
    :param end_point:
        The application end point (e.g., "connect/token" or "properties").

    :param host:
        The remote host (e.g., "api.domain.com.au").

    :param version:
        The API version (e.g., "v1").

    :param scheme:
        The connection scheme (e.g., "https").
    """
    return f"{scheme}://{host}/{version}/{end_point}"
    

def _validate_shorthand(entry, options):
    r"""
    Validate the input entry from a list of options.

    :param entry:
        A string.

    :param options:
        A list of acceptable string entries.
    """

    entry = entry.strip().lower()

    matches = []
    for option in options:
        if option.lower().strip().startswith(entry):
            matches.append(option)

    if len(matches) == 0:
        raise ValueError("unsupported option: {} (available: {})".format(entry,
            ", ".join(options)))

    elif len(matches) == 1:
        return matches[0]

    else:
        raise ValueError("multiple matches found for '{}': {} (from: {})".format(
            entry, ", ".join(matches), ", ".join(options)))


def validate_channel(channel):
    r"""
    Validate the input for property channel.

    :param channel:
        The property channel. Supported channels include: all, commercial, and
        residential.
    """
    return _validate_shorthand(channel, ("all", "commercial", "residential"))


def validate_city(city):
    r"""
    Validate the input for an Australian city.

    :param city:
        An Australian city. Supported cities include: Adelaide, Brisbane,
        Canberra, Melbourne, and Sydney.
    """
    return _validate_shorthand(city, 
        ("Adelaide", "Brisbane", "Canberra", "Melbourne", "Sydney"))