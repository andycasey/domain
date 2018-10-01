from functools import wraps
from .exceptions import AuthorisationException


def requires_scope(*scopes):
    r"""
    A decorator to specify the authorisation scopes required for a given method.

    :param scopes:
        The scopes that are required for the method. The decorator will search
        for the first available token with any of the scopes given.
    """

    def wrapper(method):

        setattr(method, "_api_scopes_", scopes)

        @wraps(method)
        def wrapped(self, *args, **kwargs):
            # If no token is supplied, then find the right one.
            kwds = kwargs.copy()
            if kwds.get("token", None) is None:
                # Find credentials with that token.
                for client_credentials in self._credentials:
                    if client_credentials.token.has_any_scope(scopes):
                        kwds["token"] = client_credentials.token
                        break
                else:
                    raise AuthorisationException(f"no authorised token found"\
                                                 f" for the required scopes "\
                                                 f"({scopes})")
                    
            return method(self, *args, **kwds)
        return wrapped

    return wrapper