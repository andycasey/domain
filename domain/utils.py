
""" General utilities. """

__all__ = ["uri"]

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
