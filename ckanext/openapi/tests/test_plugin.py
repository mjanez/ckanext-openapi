import pytest

import ckan.plugins as p
import ckanext.openapi.plugin as plugin
import ckanext.openapi.config as oa_config
from ckan.tests.helpers import reset_db

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_plugin_loaded():
    assert p.plugin_loaded("openapi")

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_update_config(monkeypatch):
    # Mock the openapi_validate_endpoints function
    def mock_openapi_validate_endpoints():
        return [{"url": "/static/openapi/sample.json", "name": "sample"}]
    
    monkeypatch.setattr(plugin, "openapi_validate_endpoints", mock_openapi_validate_endpoints)
    
    # Create an instance of the plugin and call update_config
    openapi_plugin = plugin.OpenapiPlugin()
    config_ = {}
    openapi_plugin.update_config(config_)
    
    # Check if the validated_openapi_endpoints is set correctly
    assert oa_config.validated_openapi_endpoints == [{"url": "/static/openapi/sample.json", "name": "sample"}]

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_get_blueprint():
    openapi_plugin = plugin.OpenapiPlugin()
    blueprints = openapi_plugin.get_blueprint()
    
    # Check if the blueprint is returned correctly
    assert len(blueprints) > 0
    assert blueprints[0].name == "openapi"

@pytest.mark.ckan_config("ckan.plugins", "openapi scheming_datasets")
@pytest.mark.usefixtures("with_plugins")
def test_get_helpers():
    openapi_plugin = plugin.OpenapiPlugin()
    helpers = openapi_plugin.get_helpers()
    
    # Check if the helpers are returned correctly
    assert "openapi_get_endpoints" in helpers