FROM python:3.6

MAINTAINER Daniel Leinfelder <mail@aritas.de>

ADD ./main/requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install -y git

RUN pip install -r /tmp/requirements.txt

RUN pip install uwsgi

ADD ./main /code/
WORKDIR /code