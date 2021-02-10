from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #esto es lo que muestra los errores en una pagina del navegador

ALLOWED_HOSTS = ['djangoblogpildoras.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd25ongkgdl9u4d',
        'User': 'knanctqxddzqej',
        'Password': 'b6c1b3fdf8c96b2f850462ca426c073be96a729dc5f39714072bc0b7e52def9d',
        'HOST': 'ec2-100-24-139-146.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


