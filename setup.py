# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

version = "1.0.0"

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='''ckanext-openapi''',
    version=version,
    description='''An extension to integrate documentation of the CKAN and Datastore APIs, providing Swagger UI support in the OpenAPI 2.0.0 and 3.0.0 standards.''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='''CKAN extension openapi swagger api documentation''',
    author="mjanez",
    url='https://github.com/mjanez/ckanext-openapi',
    license='AGPL',   
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    entry_points='''
        [ckan.plugins]
        openapi=ckanext.openapi.plugin:OpenapiPlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
