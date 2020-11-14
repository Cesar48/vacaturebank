from .settings import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_dsb_vacatures',
        'USER': 'localuser',
        'PASSWORD': 'BvoAsBest',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}