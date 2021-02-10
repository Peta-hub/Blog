from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #esto es lo que muestra los errores en una pagina del navegador

ALLOWED_HOSTS = ['djangoblogpildoras.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5r50tfnku1ov5',
        'User': 'foslqtzwmdvjsa',
        'Password': 'a27b4e9b4afc481dde2ef38df7e7ace7cd620c4cb93f256e5f218d655a6482a9',
        'HOST': 'ec2-67-202-63-147.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


