# html2pdf

[![Build Status](https://travis-ci.org/YauheniSobaleu/html2pdf.svg?branch=master)](https://travis-ci.org/YauheniSobaleu/html2pdf)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A REST API that converts HTML files to PDF.. Check out the project's [documentation](http://YauheniSobaleu.github.io/html2pdf/).

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

## Local Development

Start the dev server for local development:

```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

Run tests:

```bash
docker-compose run --rm web python manage.py test
```

## TODO
- Write more tests
- Generate pdf files using the celery tasks.
- Refactor the code to omit duplication.