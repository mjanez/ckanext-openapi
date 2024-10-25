import ckanext.openapi.config as oa_config

def get_helpers():
    return {
        "openapi_get_endpoints": openapi_get_endpoints,
    }

def openapi_get_endpoints():
    """Get the OpenAPI URL

    Returns:
        str: A URL if valid, otherwise None
    """
    return oa_config.validated_openapi_endpoints