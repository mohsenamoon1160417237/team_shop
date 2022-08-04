#!/bin/bash -x

export PATH="/home/team_shop_user/.local/bin:$PATH"

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations &&
  python manage.py migrate
gunicorn team_shop.wsgi:application --bind 0.0.0.0:8000
