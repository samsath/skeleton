# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(path, '../../db.sqlite'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'samhipwell@gmail.com'

# Make this unique, and don't share it with anybody.
SECRET_KEY = u'1234'


#INSTALLED_APPS = INSTALLED_APPS + (
#    'debug_toolbar',
#)


INSTALLED_APPS = INSTALLED_APPS + (
    'corsheaders',
)

MIDDLEWARE_CLASSES = ('corsheaders.middleware.CorsMiddleware',) + MIDDLEWARE_CLASSES

CORS_ORIGIN_ALLOW_ALL = True
CURRENT_SYSTEM = 'http://192.168.1.118:8000'