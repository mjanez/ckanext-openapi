import ckan.plugins as p

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
class OpenapiPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)
    p.implements(p.ITemplateHelpers)
    

    # IConfigurer
    def update_config(self, config_):
        p.toolkit.add_template_directory(config_, "templates")
        p.toolkit.add_public_directory(config_, "public")
        p.toolkit.add_resource("assets", "openapi")
        
        # Cache OpenAPI endpoints
        oa_config.validated_openapi_endpoints = openapi_validate_endpoints()

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()

    # ITemplateHelpers
    def get_helpers(self):
        return helpers.get_helpers()
