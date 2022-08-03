FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /team_shop
ENV APIDIR=/team_shop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR
#COPY . $APIDIR/

RUN chown -R team_shop_user:team_shop_group $APIDIR

ADD sh_deploy/django.sh /django.sh
RUN chmod +x /django.sh

RUN pip install --upgrade pip
