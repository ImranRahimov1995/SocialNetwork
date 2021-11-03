from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MYEMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('MYPASS')


def check_env():
    if EMAIL_HOST_USER:
    	return 'django.core.mail.backends.smtp.EmailBackend'
    else:
    	return 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = check_env()