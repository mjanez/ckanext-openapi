# ckanext-openapi. CKAN instance OpenAPI endpoints.


[![Tests](https://github.com/mjanez/ckanext-openapi/actions/workflows/test.yml/badge.svg)](https://github.com/mjanez/ckanext-openapi/actions)


The `ckanext-openapi` is an extension for CKAN that allows OpenAPI endpoints to be integrated and displayed directly from the CKAN catalogue.

!!! tip
    
    It is **recommended to use with:** [`ckan-docker`](https://github.com/mjanez/ckan-docker) deployment and [`ckanext-schemingdcat`](https://github.com/mjanez/ckanext-schemingdcat)

!!! warning

    This project requires [ckan/ckanext-scheming](https://github.com/ckan/ckanext-scheming) to work properly.

![image](./v1/img/openapi_endpoints.png)

Enhancements:

- Add custom OpenAPI endpoints directly in the CKAN deployment.
- Use `YAML` or `JSON` OpenAPI files from URLs or relative static content.