
import os
from settings import *


# django_assets 
ASSETS_ROOT = os.path.join(PROJECT_ROOT, 'static')
ASSETS_URL = ASSETS_ROOT
SASS_LOAD_PATHS = [ASSETS_ROOT + '/sass']



DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "eb3114d8-2f1d-4d67-a017-9e45fa694e09eb67744b-619e-47ac-aac6-b1ed6e12618e8ac76b7b-187a-48f4-8fa0-3b180a096a23"
NEVERCACHE_KEY = "440c3185-d407-4f31-b467-06e138b72aff30a15779-8c21-4fc7-9653-dd19d5c3b67d0dbcbb0c-f007-4ed0-a341-fe0554d74bcc"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
