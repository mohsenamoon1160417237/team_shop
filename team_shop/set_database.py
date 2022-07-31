import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def set_db(is_production: bool):
    if is_production is True:
        return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'team_psql',
            'USER': 'team_psql_user',
            'PASSWORD': 'mohsen1160417237',
            'HOST': 'postgres',
            'port': 5432
        }

    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'team_psql',
        'USER': 'team_psql_user',
        'PASSWORD': 'mohsen1160417237',
        'HOST': 'localhost',
        'PORT': 5434
    }
