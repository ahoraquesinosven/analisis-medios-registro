FROM python:3.9

WORKDIR /usr/src/app

RUN pip install Jinja2
RUN apt-get clean && apt-get update && apt-get install -y locales locales-all
