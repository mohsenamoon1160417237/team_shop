#!/bin/bash -x

RUN pip install -r requirements.txt

RUN python manage.py collectstatic

python manage.py makemigrations &&
  python manage.py migrate &&
  gunicorn team_shop.wsgi:application --bind 0.0.0.0:8000
