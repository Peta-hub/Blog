from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #esto es lo que muestra los errores en una pagina del navegador

ALLOWED_HOSTS = ['djangoblogpildoras.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')


