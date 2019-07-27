from .base import *


DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] +  MIDDLEWARE

INTERNAL_IPS = [
    '127.0.0.1',
]
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personaltools',
        'USER': 'personaltools',
        'PASSWORD': 'personaltools',
        'HOST': 'db',
        'PORT': '5432',
    }
}

SESSION_COOKIE_AGE = 31536000

#django debug toolbar override for running in docker
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}