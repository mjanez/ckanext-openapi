## Running the Tests
To run the tests:

    pytest --ckan-ini=test.ini ckanext/openapi/tests


### Run tests quickly with Docker Compose
This repository includes a Docker Compose configuration to simplify running tests. The CKAN image is built using the Dockerfile located in the `docker/` directory.

To test against the CKAN version you want to use, proceed as follows

Building the images and run the tests:

```sh
docker compose up --build
```
