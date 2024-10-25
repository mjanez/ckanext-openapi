import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


import ckanext.openapi.helpers as helpers
import ckanext.openapi.views as views
from ckanext.openapi.utils import openapi_validate_endpoints
import ckanext.openapi.config as oa_config

try:
    config_declarations = p.toolkit.blanket.config_declarations
except AttributeError:
    # CKAN 2.9 does not have config_declarations.
    # Remove when dropping support.
    def config_declarations(cls):
        return cls

@config_declarations
class OpenapiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)
    

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "openapi")
        
        # Cache OpenAPI endpoints
        oa_config.validated_openapi_endpoints = openapi_validate_endpoints()

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()

    # ITemplateHelpers
    def get_helpers(self):
        return helpers.get_helpers()
