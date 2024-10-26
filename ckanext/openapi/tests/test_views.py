import pytest
import logging

import ckanext.openapi.config as oa_config
import ckan.plugins.toolkit as tk
from ckan.tests.helpers import call_action

log = logging.getLogger(__name__)

@pytest.mark.ckan_config("ckan.plugins", "openapi")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_index(app, reset_db):
    resp = app.get(tk.h.url_for("openapi.openapi_index"))
    assert resp.status_code == 200
    assert "OpenAPI Endpoints" in resp.body.decode('utf-8')

@pytest.mark.ckan_config("ckan.plugins", "openapi")
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
    assert "Sample Endpoint" in resp.body.decode('utf-8')
    assert "Sample Description" in resp.body.decode('utf-8')

    # Test non-existing endpoint
    resp = app.get(tk.h.url_for("openapi.openapi_endpoint", name="nonexistent"), expect_errors=True)
    assert resp.status_code == 404
    assert "OpenAPI endpoint nonexistent not found" in resp.body.decode('utf-8')