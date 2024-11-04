import json
import logging
from urllib.parse import urljoin

import ckan.plugins as p
from ckan.lib import helpers as ckan_helpers

import ckanext.openapi.config as oa_config

log = logging.getLogger(__name__)


OPENAPI_REQUIRED_KEYS = ['url', 'name', 'title', 'description']

def get_not_lang_root_path():
    """
    Retrieve the root path from the CKAN configuration, removing the '{{LANG}}' placeholder if present.

    This function fetches the 'ckan.root_path' configuration setting and removes the '/{{LANG}}' 
    placeholder if it exists in the path.

    Returns:
        str: The root path with the '{{LANG}}' placeholder removed if it was present.
    """
    root_path = p.toolkit.config.get('ckan.root_path')
    
    # Removes the '{{LANG}}' part if present in the root_path
    if root_path and '{{LANG}}' in root_path:
        root_path = root_path.replace('/{{LANG}}', '')
    
    return root_path

def openapi_is_valid_endpoint(endpoint):
    """
    Validates that an endpoint dictionary has the required keys and types.

    Args:
        Endpoint (dict): The endpoint dictionary to validate.

    Returns
        Boolean: True if the endpoint is valid, false otherwise.
    """
    required_lang = p.toolkit.config.get("ckan.locale_default", "en")
    
    if not isinstance(endpoint, dict):
        log.error('Not dict: %s', endpoint)
        return False
    for key in OPENAPI_REQUIRED_KEYS:
        if key not in endpoint or not isinstance(endpoint[key], dict if key in ['title', 'description'] else str):
            log.error(f"Missing {key} or invalid type")
            return False
    if not all(isinstance(endpoint[key].get(required_lang), str) for key in ['title', 'description']):
        log.error(f"Missing 'description' for language '{required_lang}'")
        return False
    return True

def construct_full_url(url, protocol, host, root_path=''):
    """
    Constructs a full URL from a relative URL.

    Args:
        url (str): The URL to process.
        protocol (str): The protocol (http or https).
        host (str): The CKAN host.
        root_path (str): The root path of CKAN.

    Returns:
        str: The full URL.
    """
    if url.startswith('http://') or url.startswith('https://'):
        return url

    base = f"{protocol}://{host}/"
    if root_path:
        base = urljoin(base, root_path.rstrip('/') + '/')
    full_url = urljoin(base, url.lstrip('/'))
    return full_url

def openapi_validate_endpoints():
    """
    Valida si el valor es una cadena JSON que representa una lista de diccionarios con las claves requeridas.
    Si el valor no es válido, devuelve una lista por defecto de endpoints de OpenAPI.

    Returns:
        list: La lista validada de endpoints de OpenAPI o la lista por defecto si es inválida.
    """
    endpoints = p.toolkit.config.get('ckanext.openapi.endpoints')
    
    if endpoints is None:
        endpoints = oa_config.validated_openapi_endpoints or oa_config.default_openapi_endpoints
    
    if isinstance(endpoints, str):
        try:
            endpoints = json.loads(endpoints)
        except (json.JSONDecodeError, TypeError) as e:
            log.error('Error parsing openapi_endpoints: %s', e)
            return oa_config.default_openapi_endpoints
        
    if not isinstance(endpoints, list):
        log.error('openapi_endpoints is not a list')
        return oa_config.default_openapi_endpoints

    protocol, host = ckan_helpers.get_site_protocol_and_host()
    root_path = get_not_lang_root_path()

    validated_endpoints = []
    for endpoint in endpoints:
        if not openapi_is_valid_endpoint(endpoint):
            log.error('Invalid endpoint: %s', endpoint)
            return oa_config.default_openapi_endpoints
        
        endpoint['url'] = construct_full_url(endpoint['url'], protocol, host, root_path)
        validated_endpoints.append(endpoint)

    return validated_endpoints