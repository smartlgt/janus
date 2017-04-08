#!/bin/sh

docker-compose run --rm web /usr/local/bin/python /code/manage.py collectstatic