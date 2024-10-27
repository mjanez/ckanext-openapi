import pytest
import logging
import ckanext.openapi.config as oa_config
import ckan.plugins.toolkit as tk
from ckan.tests.helpers import call_action

log = logging.getLogger(__name__)

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_index(app, reset_db):
    resp = app.get(tk.h.url_for("openapi.openapi_index"))
    assert resp.status_code == 200
    assert "OpenAPI Endpoints" in resp.body
    assert "The OpenAPI Specification (OAS) defines a standard" in resp.body
    assert "OpenAPI Specification" in resp.body
    assert "ckanext-openapi" in resp.body

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_endpoint(app, reset_db, monkeypatch):
    # Mock the validated_openapi_endpoints
    endpoints = [
        {"url": "/static/openapi/sample.json", "name": "sample", "title": {"en": "Sample Endpoint"}, "description": {"en": "Sample Description"}}
    ]
    monkeypatch.setattr(oa_config, "validated_openapi_endpoints", endpoints)

    # Test existing endpoint
    resp = app.get(tk.h.url_for("openapi.openapi_endpoint", name="sample"))
    assert resp.status_code == 200

    # Print the response content for debugging
    print(resp.body)

    assert endpoints[0]['url'] in resp.body

    # Test non-existing endpoint
    resp = app.get(tk.h.url_for("openapi.openapi_endpoint", name="nonexistent"), expect_errors=True)
    assert resp.status_code == 404
    assert "OpenAPI endpoint nonexistent not found" in resp.body

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_index_no_endpoints(app, reset_db, monkeypatch):
    # Mock the validated_openapi_endpoints with an empty list
    monkeypatch.setattr(oa_config, "validated_openapi_endpoints", [])

    resp = app.get(tk.h.url_for("openapi.openapi_index"))
    assert resp.status_code == 200
    assert "Not OpenAPI endpoints available" in resp.body
    assert "To retrieve them, check the <code>ckan.ini</code> config file" in resp.body

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_endpoint_swagger_ui(app, reset_db, monkeypatch):
    # Mock the validated_openapi_endpoints
    endpoints = [
        {"url": "/static/openapi/sample.json", "name": "sample", "title": {"en": "Sample Endpoint"}, "description": {"en": "Sample Description"}}
    ]
    monkeypatch.setattr(oa_config, "validated_openapi_endpoints", endpoints)

    # Test Swagger UI rendering
    resp = app.get(tk.h.url_for("openapi.openapi_endpoint", name="sample"))
    assert resp.status_code == 200

    # Verifica que el contenedor de Swagger UI esté presente
    assert '<div id="swagger-ui">' in resp.body
    assert endpoints[0]['url'] in resp.body
    assert '<link href="/webassets/ckanext-openapi/' in resp.body
    assert '<script src="/webassets/ckanext-openapi/' in resp.body