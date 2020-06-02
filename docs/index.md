# html2pdf

[![Build Status](https://travis-ci.org/YauheniSobaleu/html2pdf.svg?branch=master)](https://travis-ci.org/YauheniSobaleu/html2pdf)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A REST API that converts HTML files to PDF.. Check out the project's [documentation](http://YauheniSobaleu.github.io/html2pdf/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

Run tests:

```bash
docker-compose run --rm web python manage.py test
```