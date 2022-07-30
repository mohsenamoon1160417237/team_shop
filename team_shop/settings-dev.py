from .settings import *

from .set_database import set_db

DATABASES = {
    'default': set_db(False)
}
