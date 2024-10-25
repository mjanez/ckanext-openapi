[![Tests](https://github.com/mjanez/ckanext-openapi/workflows/Tests/badge.svg?branch=main)](https://github.com/mjanez/ckanext-openapi/actions)

# ckanext-openapi

The `ckanext-openapi` is an extension for CKAN that allows OpenAPI endpoints to be integrated and displayed directly from the CKAN catalogue.

- [OpenAPI Specification](https://swagger.io/specification/)

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


## Config settings
Set the endpoints you want to use with configuration options:

  ```ini
  # Each of the plugins is optional depending on your use
  ckan.plugins = '[{"url":"/static/openapi/sample.json","name":"sample","title":{"en":"OpenAPI sample 1","es":"Ejemplo de OpenAPI 1"},"description":{"en":"API with examples.","es":"API con ejemplos."}},{"url":"https://raw.githubusercontent.com/OAI/OpenAPI-Specification/refs/heads/main/examples/v3.0/petstore.json","name":"petstore","title":{"en":"Petstore OpenAPI example","es":"Ejemplo OpenAPI Petstore"},"description":{"en":"This is a sample Pet Store Server based on the OpenAPI 3.0 specification.","es":"Este es un ejemplo de Servidor de Tienda de Mascotas basado en la especificación OpenAPI 3.0."}}]'
  ```



## Developer installation

To install `ckanext-openapi` for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/mjanez/ckanext-openapi.git
    cd ckanext-openapi
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-openapi

If `ckanext-openapi` should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
