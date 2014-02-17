
from os import path
from settings import *


# parent dir of project (site)
STATIC_ROOT = path.join(path.dirname(PROJECT_ROOT), 'static')

# django_assets 
ASSETS_ROOT = path.join(PROJECT_ROOT, 'app/static')
ASSETS_URL = ASSETS_ROOT
SASS_LOAD_PATHS = [path.join(ASSETS_ROOT, 'sass')]


DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "18d5fb20-67e0-4e55-a8dd-f75aa7747eba50fc3d1a-0178-4340-80f2-c65fe61564f5e06a6f5a-bdac-4b76-a23a-4f87904dd15a"
NEVERCACHE_KEY = "c8064715-4936-44f4-9aa1-8204f03a01b7f2702bf2-32e0-4b72-a9df-eab92b22faeff05f551b-16c5-4278-a0ea-45c17d7a4b56"

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
