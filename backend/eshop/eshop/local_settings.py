from django.conf import settings

DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = settings.INSTALLED_APPS

INSTALLED_APPS += [
    'django_extensions',
]

CORS_ORIGIN_ALLOW_ALL = True
