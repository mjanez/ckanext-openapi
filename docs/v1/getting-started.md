# Getting started

## Requirements
### Compatibility
Compatibility with core CKAN versions:

| CKAN version | Compatible?                                                                 |
|--------------|-----------------------------------------------------------------------------|
| 2.8          | ❌ No (>= Python 3)                                                          |
| 2.9          | ❌ No [(>= CKAN 2.10)](https://github.com/mjanez/ckanext-openapi/actions/runs/11540091283)
| 2.10         | ✅ Yes  |
| 2.11         | ✅ Yes  |

### Plugins
This plugin needs the following plugins to work properly:

  ```sh
  # Install latest stable release of:
  ## ckan/ckanext-scheming: https://github.com/ckan/ckanext-scheming/tags (e.g. release-3.0.0)
  pip install -e git+https://github.com/ckan/ckanext-scheming.git@release-3.0.0#egg=ckanext-scheming
  ```

## Installation

To install `ckanext-openapi`:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/mjanez/ckanext-openapi.git
    cd ckanext-openapi
    pip install -e .
    pip install -r requirements.txt

3. Clone the source of `ckanext-scheming` to work properly:

    git clone https://github.com/ckan/ckanext-scheming.git
    cd ckanext-scheming
    pip install -e .
    pip install -r requirements.txt

4. Add `openapi` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`). And `scheming_datasets` if not using `schemingdcat` and `schemingdcat_datasets` from [`ckanext-schemingdcat`](https://github.com/mjanez/ckanext-schemingdcat?tab=readme-ov-file#configuration) extension.

    ```ini
    # Add the plugin to the list of plugins
    ckan.plugins = ... scheming_datasets ... openapi
    ```

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

## PIP installation
  ```sh
  cd $CKAN_VENV/src/

  # Install latest stable release of:
  ## ckan/ckanext-scheming: https://github.com/ckan/ckanext-scheming/tags (e.g. release-3.0.0)
  pip install -e git+https://github.com/ckan/ckanext-scheming.git@release-3.0.0#egg=ckanext-scheming

  # Install the ckanext-openapi plugin
  pip install -e "git+https://github.com/ckan/ckanext-openapi.git#egg=ckanext-openapi"
  ```

## Config settings
Set the endpoints you want to use with configuration options:

  ```ini
  # Each of the plugins is optional depending on your use
  ckanext.openapi.endpoints = '[{"url":"/static/openapi/sample.json","name":"sample","title":{"en":"OpenAPI sample 1","es":"Ejemplo de OpenAPI 1"},"description":{"en":"API with examples.","es":"API con ejemplos."}},{"url":"https://raw.githubusercontent.com/OAI/OpenAPI-Specification/refs/heads/main/examples/v3.0/petstore.json","name":"petstore","title":{"en":"Petstore OpenAPI example","es":"Ejemplo OpenAPI Petstore"},"description":{"en":"This is a sample Pet Store Server based on the OpenAPI 3.0 specification.","es":"Este es un ejemplo de Servidor de Tienda de Mascotas basado en la especificación OpenAPI 3.0."}}]'
  ```

Or using [`ckanext-ennvars`](https://github.com/ckan/ckanext-envvars):

```bash
CKANEXT__OPENAPI__ENDPOINTS='[{"url":"https://raw.githubusercontent.com/mjanez/ckanext-openapi/refs/heads/develop/ckanext/openapi/public/static/openapi/datastore.yaml","name":"datastore","title":{"en":"CKAN - Datastore API","es":"Portal de datos abiertos de CKAN - API Datastore"},"description":{"en":"This API provides live access to the Datastore portion of the CKAN Open Data Portal.","es":"Esta API proporciona acceso en tiempo real a la parte de Datastore del Portal de Datos Abiertos CKAN."}},{"url":"https://raw.githubusercontent.com/mjanez/ckanext-openapi/refs/heads/develop/ckanext/openapi/public/static/openapi/ckan.yaml","name":"ckan","title":{"en":"CKAN Open Data Portal - CKAN API (ES)","es":"Portal de datos abiertos de CKAN - API CKAN"},"description":{"en":"This API provides live access to the CKAN portion of the CKAN Open Data Portal.","es":"Esta API proporciona acceso en tiempo real a la parte de CKAN del Portal de Datos Abiertos CKAN."}}]'
```
