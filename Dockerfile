FROM python:3.12-alpine3.19
ENV PYTHONBUFFERED=1
ARG UID=0
ARG GID=0

WORKDIR /code

RUN \
    pip install --upgrade pip setuptools wheel  && \
    pip install grpcio==1.59.0
