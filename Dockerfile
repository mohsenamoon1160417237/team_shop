FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /teamShop
ENV APIDIR=/teamShop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR
COPY . $APIDIR/

RUN addgroup --group teamShop_group

RUN useradd -ms /bin/bash teamShop_user
RUN adduser teamShop_user teamShop_group

RUN chown -R teamShop_user:teamShop_group $APIDIR

ADD sh_deploy/django.sh /django.sh
RUN chmod +x /django.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER teamShop_user
