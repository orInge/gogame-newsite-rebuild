
from os import path
from os import environ
from settings import *


##################
# AWS S3 STORAGE #
##################

# django_storages (boto)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# enable collectstatic to automatically upload static assets to AWS bucket
STATICFILES_STORAGE = 's3static.S3Static'

AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = 'gogame-newsite-rebuild'

STATIC_ROOT = 'http://%s.s3.amazonaws.com/static', AWS_STORAGE_BUCKET_NAME


# bugfix for gunicorn workers
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}


############# 
# LOCAL DEV #
#############

DEBUG = True

# parent dir of project (site)
# STATIC_ROOT = path.join(path.dirname(PROJECT_ROOT), 'static')

# django_assets 
ASSETS_ROOT = path.join(PROJECT_ROOT, 'app/static')
ASSETS_URL = ASSETS_ROOT
SASS_LOAD_PATHS = [path.join(ASSETS_ROOT, 'sass')]


############
# DATABASE #
############

# Make these unique, and don't share it with anybody.
SECRET_KEY = "18d5fb20-67e0-4e55-a8dd-f75aa7747eba50fc3d1a-0178-4340-80f2-c65fe61564f5e06a6f5a-bdac-4b76-a23a-4f87904dd15a"
NEVERCACHE_KEY = "c8064715-4936-44f4-9aa1-8204f03a01b7f2702bf2-32e0-4b72-a9df-eab92b22faeff05f551b-16c5-4278-a0ea-45c17d7a4b56"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "newsite_rebuild",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

ALLOWED_HOSTS = ['rebuild:8000']
