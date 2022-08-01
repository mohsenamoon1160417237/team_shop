#!/bin/bash -x

python manage.py makemigrations &&
  python manage.py migrate &&
  python manage.py collectstatic --noinput &&
  service nginx start &&
  gunicorn team_shop.wsgi:application --bind 0.0.0.0:8000
