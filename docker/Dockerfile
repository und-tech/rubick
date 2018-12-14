FROM python:3.5.6-alpine3.8

RUN apk update && apk add --no-cache git

ADD . /ant

WORKDIR /ant
RUN python3 setup.py install

WORKDIR /tmp/ant

ENTRYPOINT ["ant"]