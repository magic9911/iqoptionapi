"""Module for IQ Option http auth resource."""

from iqoptionapi2.http.resource import Resource


class Auth(Resource):
    """Class for IQ Option http auth resource."""
    # pylint: disable=too-few-public-methods

    url = "auth"
