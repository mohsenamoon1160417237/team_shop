#!/bin/bash -x

pip install --upgrade pip
sudo -H pip install virtualenv

virtualenv team_shop_env
source team_shop_env/bin/activate

su -c team_shop_user

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput

python manage.py makemigrations &&
  python manage.py migrate
gunicorn team_shop.wsgi:application --bind 0.0.0.0:8000
