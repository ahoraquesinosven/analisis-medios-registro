FROM python:3.12

WORKDIR /usr/src/app

RUN pip install tldextract pandas
