# ckanext-openapi

[![Tests](https://github.com/mjanez/ckanext-openapi/workflows/Tests/badge.svg?branch=main)](https://github.com/mjanez/ckanext-openapi/actions)
[![Code Coverage](http://codecov.io/github/ckan/ckanext-openapi/coverage.svg?branch=main)](http://codecov.io/github/ckan/ckanext-openapi?branch=main)

`ckanext-openapi` is an extension for CKAN that integrates and displays OpenAPI endpoints directly in the CKAN catalog, [^1] supporting both **OpenAPI 2.0.0** and **OpenAPI 3.0.0** specifications.

- [OpenAPI Specification](https://swagger.io/specification/)


> [!IMPORTANT]
> Read the documentation for a full user guide:
> https://mjanez.github.io/ckanext-openapi

> [!WARNING] 
> This project requires [ckan/ckanext-scheming](https://github.com/ckan/ckanext-scheming) to work properly.

## Overview

In terms of CKAN features, this extension offers:

* Provides an OpenAPI/Swagger UI interface for custom APIs, e.g: CKAN and Datastore.
* Allows configuration of custom OpenAPI endpoints.
* Supports multi-language documentation fields.
* Integrates OpenAPI in CKAN Open Data portal.

## Running the Tests

To run the tests do:

    pytest --ckan-ini=test.ini ckanext/openapi/tests

## Releases

To create a new release, follow these steps:

* Determine new release number based on the rules of [semantic versioning](http://semver.org)
* Update the CHANGELOG, especially the link for the "Unreleased" section
* Update the version number in `setup.py`
* Create a new release on GitHub and add the CHANGELOG of this release as release notes

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

## Copying and License

This material is copyright (c) Open Knowledge.

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

http://www.fsf.org/licensing/licenses/agpl-3.0.html

[^1] Inspired by `ckanext-openapiview` template. Info and greetings to: https://github.com/open-data/ckanext-openapiview