import logging

import ckanext.openapi.config as oa_config
from ckan.plugins import toolkit

log = logging.getLogger(__name__)

def get_helpers():
    return {
        "openapi_get_endpoints": openapi_get_endpoints,
    }

def openapi_get_endpoints():
    """Get the OpenAPI endpoints list of dicts.

    Returns:
        list: A list of dictionaries representing the OpenAPI endpoints if valid, otherwise an empty list.
    """
    if oa_config.validated_openapi_endpoints is not None:
        return oa_config.validated_openapi_endpoints
    return oa_config.default_openapi_endpoints