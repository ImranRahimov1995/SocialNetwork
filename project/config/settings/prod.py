from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key

DEBUG = False

ALLOWED_HOSTS = [os.getenv('PUBLIC_IP' ,'*')]


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.getenv('DB_APP','app_db'),
         'USER': os.getenv('DB_USER','admin'),
         'PASSWORD': os.getenv('DB_PASSWORD','devpass'),
         'HOST': os.getenv("DB_HOST","postgresdb"),
         'PORT': os.getenv("DB_PORT","5432"),
     }
}
