
<!-- start-config -->


### General settings


#### ckanext.openapi.endpoints

List of OpenAPI endpoints. Each endpoint should be a dictionary with the following keys:

- `url`, str: URL or relative path of the OpenAPI file, accepted formats are JSON and YAML, e.g. `https://raw.githubusercontent.com/OAI/OpenAPI-Specification/refs/heads/main/examples/v3.0/petstore.json` or `/static/openapi/sample.yaml`
- `name`, str: Path of the OpenAPI in CKAN Open Data portal, e.g. `ckan`
- `title`, dict: Title for the endpoint in different languages, e.g. `{'en': 'CKAN OpenAPI', 'es': 'Punto final OpenAPI de CKAN'}`
- `description`, dict: Description for the endpoint in different languages, e.g. `{'en': 'CKAN OpenAPI description', 'es': 'Descripción de OpenAPI CKAN'}`

<!-- end-config -->