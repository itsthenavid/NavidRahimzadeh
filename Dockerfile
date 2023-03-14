# syntax=docker/dockerfile:1

FROM python

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install gettext

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ="Asia/Tehran"

RUN mkdir /code/
WORKDIR /code

ADD requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt

ADD . /code/
