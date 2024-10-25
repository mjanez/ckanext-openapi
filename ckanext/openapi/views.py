import logging
from flask import Blueprint

from ckan.plugins.toolkit import render, g
import ckan.lib.base as base

import ckanext.openapi.config as oa_config

log = logging.getLogger(__name__)


openapi = Blueprint(
    "openapi", __name__)

def openapi_index():
    return render('openapi/openapi/index.html')

def openapi_endpoint(name):
    """
    Renders the OpenAPI documentation for a specific endpoint.

    Args:
        name (str): The name of the OpenAPI endpoint.

    Returns:
        str: The rendered HTML for the OpenAPI documentation.
    """
    log.debug('function openapi_endpoint: %s', name)
    endpoints = oa_config.schemingdcat_get_openapi_endpoints()
    log.debug('openapi_endpoint: %s', endpoints)
    endpoint = next((ep for ep in endpoints if ep['name'] == name), None)
    if not endpoint:
        log.debug('OpenAPI endpoint {name} not found'.format(name=name))
        return base.abort(404, (u'OpenAPI endpoint {name} not found').format(name=name))
    
    return render('openapi/openapi/openapi_endpoint.html', extra_vars={
        'endpoint': endpoint
    })

# Rules
openapi.add_url_rule("/openapi", view_func=openapi_index, endpoint="openapi_index", strict_slashes=False)
openapi.add_url_rule("/openapi/<name>", view_func=openapi_endpoint, endpoint="openapi_endpoint", strict_slashes=False)

def get_blueprints():
    return [openapi]
