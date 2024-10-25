"""Tests for views.py."""

import pytest

import ckanext.openapi.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "openapi")
@pytest.mark.usefixtures("with_plugins")
def test_openapi_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("openapi.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, openapi!"
