from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def set_db(is_production: bool):
    if is_production is True:
        return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': 'postgres',
            'port': 5432
        }

    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5434
    }
