import pytest
import json
from unittest.mock import patch
from ckanext.openapi.utils import (
    openapi_is_valid_endpoint,
    construct_full_url,
    openapi_validate_endpoints,
    get_not_lang_root_path
)

@pytest.mark.ckan_config("ckan.locale_default", "en")
def test_openapi_is_valid_endpoint():
    valid_endpoint = {
        "url": "http://example.com/api",
        "name": "example",
        "title": {"en": "Example API", "es": "API de ejemplo"},
        "description": {"en": "An example API", "es": "Una API de ejemplo"}
    }
    invalid_endpoint = [
        "http://example.com/api",
        "example",
        "An example API"
    ] # Object is not a dictionary
    invalid_endpoint_required_lang = {
        "url": "http://example.com/api",
        "name": "example",
        "title": {"en": "Example API", "es": "API de ejemplo"},
        "description": {"es": "Example API"}  # Missing description for required lang
    }
    invalid_endpoint_missing_key = {
        "url": "http://example.com/api",
        "name": "example",
        # Missing required key title
        "description": {"en": "An example API"}
    }

    assert openapi_is_valid_endpoint(valid_endpoint) is True
    assert openapi_is_valid_endpoint(invalid_endpoint) is False
    assert openapi_is_valid_endpoint(invalid_endpoint_required_lang) is False
    assert openapi_is_valid_endpoint(invalid_endpoint_missing_key) is False

def test_construct_full_url_with_trailing_slash_in_root_path():
    url = "/api"
    protocol = "https"
    host = "example.com"
    root_path = "ckan/"
    
    full_url = construct_full_url(url, protocol, host, root_path)
    assert full_url == "https://example.com/ckan/api"

def test_construct_full_url_without_protocol():
    url = "api/resource"
    protocol = "https"
    host = "example.com"
    root_path = "ckan"
    
    full_url = construct_full_url(url, protocol, host, root_path)
    assert full_url == "https://example.com/ckan/api/resource"

def test_construct_full_url():
    url = "/api"
    protocol = "https"
    host = "example.com"
    root_path = "ckan"

    # Caso con root_path
    full_url_with_root = construct_full_url(url, protocol, host, root_path)
    assert full_url_with_root == "https://example.com/ckan/api"

    # Caso sin root_path
    full_url_no_root = construct_full_url(url, protocol, host)
    assert full_url_no_root == "https://example.com/api"

    # Caso con URL absoluta
    absolute_url = "http://example.com/api"
    assert construct_full_url(absolute_url, protocol, host) == absolute_url

    # Caso con root_path vacío
    full_url_empty_root = construct_full_url(url, protocol, host, "")
    assert full_url_empty_root == "https://example.com/api"

    # Caso con root_path con barra al final
    root_path_with_slash = "ckan/"
    full_url_with_slash = construct_full_url(url, protocol, host, root_path_with_slash)
    assert full_url_with_slash == "https://example.com/ckan/api"

@patch('ckanext.openapi.utils.p.toolkit.config.get')
@patch('ckanext.openapi.utils.oa_config')
@patch('ckanext.openapi.utils.ckan_helpers.get_site_protocol_and_host')
def test_openapi_validate_endpoints(mock_get_site_protocol_and_host, mock_oa_config, mock_config_get):
    mock_get_site_protocol_and_host.return_value = ("https", "example.com")
    mock_config_get.side_effect = lambda key, default=None: {
        'ckanext.openapi.endpoints': json.dumps([
            {"url": "/api", "name": "example", "title": {"en": "Example API"}, "description": {"en": "An example API"}}
        ])
    }.get(key, default)
    mock_oa_config.validated_openapi_endpoints = []
    mock_oa_config.default_openapi_endpoints = [
        {"url": "http://default.com/api", "name": "default", "title": {"en": "Default API"}, "description": {"en": "A default API"}}
    ]

    endpoints = openapi_validate_endpoints()
    assert len(endpoints) == 1
    assert endpoints[0]['url'] == "https://example.com/api"
    assert endpoints[0]['name'] == "example"

    # Test with invalid JSON
    mock_config_get.side_effect = lambda key, default=None: {
        'ckanext.openapi.endpoints': "invalid json"
    }.get(key, default)
    endpoints = openapi_validate_endpoints()
    assert endpoints == mock_oa_config.default_openapi_endpoints

    # Test with no endpoints in config
    mock_config_get.side_effect = lambda key, default=None: {
        'ckanext.openapi.endpoints': None
    }.get(key, default)
    endpoints = openapi_validate_endpoints()
    assert endpoints == mock_oa_config.default_openapi_endpoints

    # Test with invalid endpoint structure
    mock_config_get.side_effect = lambda key, default=None: {
        'ckanext.openapi.endpoints': json.dumps(
            {"url": "/api", "name": "example", "title": "Example API", "description": {"en": "An example API"}}  # Invalid object type, is not a list
        )
    }.get(key, default)
    endpoints = openapi_validate_endpoints()
    assert endpoints == mock_oa_config.default_openapi_endpoints
    
@patch('ckanext.openapi.utils.p.toolkit.config.get')
@patch('ckanext.openapi.utils.oa_config')
@patch('ckanext.openapi.utils.ckan_helpers.get_site_protocol_and_host')
def test_openapi_validate_endpoints_invalid_structure(mock_get_site_protocol_and_host, mock_oa_config, mock_config_get):
    mock_get_site_protocol_and_host.return_value = ("https", "example.com")
    mock_config_get.side_effect = lambda key, default=None: {
        'ckanext.openapi.endpoints': json.dumps([
            {"url": "/api", "name": "example", "title": "Example API", "description": {"en": "An example API"}}  # Tipo de título inválido
        ])
    }.get(key, default)
    mock_oa_config.validated_openapi_endpoints = []
    mock_oa_config.default_openapi_endpoints = [
        {"url": "http://default.com/api", "name": "default", "title": {"en": "Default API"}, "description": {"en": "A default API"}}
    ]
    
    endpoints = openapi_validate_endpoints()
    assert endpoints == mock_oa_config.default_openapi_endpoints

@patch('ckanext.openapi.utils.p.toolkit.config.get')
def test_get_not_lang_root_path(mock_config_get):
    # Test with root_path containing '{{LANG}}'
    mock_config_get.return_value = '/ckan/{{LANG}}'
    root_path = get_not_lang_root_path()
    assert root_path == '/ckan'

    # Test with root_path not containing '{{LANG}}'
    mock_config_get.return_value = '/ckan'
    root_path = get_not_lang_root_path()
    assert root_path == '/ckan'

    # Test with root_path being None
    mock_config_get.return_value = None
    root_path = get_not_lang_root_path()
    assert root_path is None