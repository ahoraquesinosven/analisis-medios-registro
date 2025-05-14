FROM python:3.9

WORKDIR /usr/src/app

RUN pip install tldextract
RUN apt-get clean && apt-get update && apt-get install -y locales locales-all
