FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /team_shop
ENV APIDIR=/team_shop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR
COPY . $APIDIR/

RUN groupadd -g 998 docker
RUN useradd team_shop_user -u 1000 -g 998 -m -s /bin/bash

RUN chown -R 1000:998 $APIDIR

ADD sh_deploy/django.sh /django.sh
RUN chmod +x /django.sh

RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
#RUN python manage.py collectstatic --noinput

USER team_shop_user
