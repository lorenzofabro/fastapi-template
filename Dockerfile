FROM python:3.10.2-alpine3.15

# Define ARGs
ARG ENVIRONMENT=local

# Python logs to STDOUT
ENV PYTHONUNBUFFERED 1

# Sane defaults for pip
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apk update && apk upgrade &&\
    apk add build-base libressl-dev gcc git openssh-client linux-headers libffi-dev gcc musl-dev python3-dev &&\
    pip install pip setuptools

COPY requirements/*.txt /tmp/requirements/

RUN pip install -r /tmp/requirements/base.txt &&\
    if [ $ENVIRONMENT = local ]; then \
    pip install -r /tmp/requirements/dev.txt;\
    pip install -r /tmp/requirements/test.txt;\
    fi

WORKDIR /app

COPY . .

CMD [ "python", "config/main.py" ]