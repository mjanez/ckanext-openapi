"""Tests for helpers.py."""

import ckanext.openapi.helpers as helpers


def test_openapi_hello():
    assert helpers.openapi_hello() == "Hello, openapi!"
