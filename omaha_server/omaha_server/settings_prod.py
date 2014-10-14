# coding: utf8

import os

from settings import *

DEBUG = False

ALLOWED_HOSTS = (os.environ['HOST_NAME'], '*')
SECRET_KEY = os.environ['SECRET_KEY']

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = S3_URL
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_IS_GZIPPED = True

SUIT_CONFIG = {
    'ADMIN_NAME': 'Omaha Server [{}]'.format(os.environ.get('APP_VERSION')),
}

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_DNS'),
}

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)