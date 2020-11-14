from .settings import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dsb_vacatures',
        'USER': 'webuser',
        'PASSWORD': 'BvoAsBest',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}