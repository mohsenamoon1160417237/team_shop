FROM python:3.9

RUN mkdir /team_shop
ENV APIDIR=/team_shop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR
#COPY . $APIDIR/

RUN groupadd -g 998 docker
RUN useradd team_shop_user -u 1000 -g 998 -m -s /bin/bash

RUN chown -R 1000:998 $APIDIR

USER team_shop_user

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

