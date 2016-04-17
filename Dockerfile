FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD RUN pip install --no-cache-dir

ONBUILD COPY . /usr/src/app
RUN pip install tweepy
