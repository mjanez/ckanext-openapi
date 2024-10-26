# Getting started

## Requirements
### Compatibility
Compatibility with core CKAN versions:

| CKAN version | Compatible?                                                                 |
|--------------|-----------------------------------------------------------------------------|
| 2.8          | ❌ No (>= Python 3)                                                          |
| 2.9          | ✅ Yes  |
| 2.10         | ✅ Yes  |

### Plugins
This plugin needs the following plugins to work properly:

## Installation

To install `ckanext-openapi`:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/mjanez/ckanext-openapi.git
    cd ckanext-openapi
    pip install -e .
	pip install -r requirements.txt

3. Add `openapi` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

    ```ini
    # Add the plugin to the list of plugins
    ckan.plugins = ... dcat ... openapi
    ```

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

## PIP installation
  ```sh
  cd $CKAN_VENV/src/

  # Install the scheming_dataset plugin
  pip install -e "git+https://github.com/ckan/ckanext-openapi.git#egg=ckanext-openapi"
  ```

## Config settings
Set the endpoints you want to use with configuration options:

  ```ini
  # Each of the plugins is optional depending on your use
  ckan.plugins = '[{"url":"/static/openapi/sample.json","name":"sample","title":{"en":"OpenAPI sample 1","es":"Ejemplo de OpenAPI 1"},"description":{"en":"API with examples.","es":"API con ejemplos."}},{"url":"https://raw.githubusercontent.com/OAI/OpenAPI-Specification/refs/heads/main/examples/v3.0/petstore.json","name":"petstore","title":{"en":"Petstore OpenAPI example","es":"Ejemplo OpenAPI Petstore"},"description":{"en":"This is a sample Pet Store Server based on the OpenAPI 3.0 specification.","es":"Este es un ejemplo de Servidor de Tienda de Mascotas basado en la especificación OpenAPI 3.0."}}]'
  ```