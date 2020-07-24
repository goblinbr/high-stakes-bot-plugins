FROM python:3.7.8-slim-buster

LABEL maintainer="Rodrigo de Bona Sartor <rodrigo.goblin@gmail.com>"

ENV PATH /app/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get update \
    && apt-get -y install git \
    && pip3 install errbot

RUN mkdir errbot && cd errbot && errbot --init && rm -rf scripts/*

WORKDIR /errbot

ENTRYPOINT ["errbot"]
