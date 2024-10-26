# tests/test_helpers.py
import pytest
from ckan.plugins import toolkit
import ckanext.openapi.helpers as helpers
import ckanext.openapi.config as oa_config

def test_openapi_get_endpoints_valid_list(monkeypatch):
    """Test that openapi_get_endpoints returns a valid List."""

    # Mock the validated_openapi_endpoints in oa_config
    mock_list =  [{"url":"/static/openapi/sample.json","name":"sample","title":{"en":"Sample OpenAPI with examples","es":"Ejemplo de OpenAPI"},"description":{"en":"Description of the OpenAPI 1","es":"Descripcion del OpenAPI 1"}},{"url":"https://raw.githubusercontent.com/OAI/OpenAPI-Specification/refs/heads/main/examples/v3.0/petstore.json","name":"datastore","title":{"en":"Petstore OpenAPI","es":"OpenAPI Petstore"},"description":{"en":"Petsore OpenAPI sample.","es":"Ejemplo de OpenAPI de Petstore."}}]
    monkeypatch.setattr(oa_config, "validated_openapi_endpoints", mock_list)

    # Call the helper function
    result = helpers.openapi_get_endpoints()

    # Assert the result is the mocked URL
    assert result == mock_list, "Expected the helper to return the valid OpenAPI endpoints list"


def test_openapi_get_endpoints_no_list(monkeypatch):
    """Test that openapi_get_endpoints returns default when no valid list of endpoints is provided."""

    # Mock the validated_openapi_endpoints to None
    monkeypatch.setattr(oa_config, "validated_openapi_endpoints", None)

    # Set a specific value for default_openapi_endpoints for the test
    expected_default_endpoints = [{"url": "/static/openapi/sample.json", "name": "sample"}]
    monkeypatch.setattr(oa_config, "default_openapi_endpoints", expected_default_endpoints)

    # Call the helper function
    result = helpers.openapi_get_endpoints()

    # Assert the result is the expected default endpoints
    assert result == expected_default_endpoints, "Expected the helper to return oa_config.default_openapi_endpoints when no URL is configured"
