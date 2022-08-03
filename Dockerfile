FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /team_shop
ENV APIDIR=/team_shop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR

RUN groupadd -g 1001 team_shop_user
RUN useradd team_shop_user -u 1000 -g 1001 -m -s /bin/bash

RUN chown -R 1000:1001 $APIDIR

ADD sh_deploy/django.sh /django.sh
RUN chmod +x /django.sh

RUN pip install --upgrade pip

USER team_shop_user
