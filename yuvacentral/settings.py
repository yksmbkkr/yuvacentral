"""
Django settings for yuvacentral project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath
from .aws_key import *
from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'db4ed6e0-d452-4efc-88b9-85d802a554ca'

# SECURITY WARNING: don't run with debug turned on in production!
if os.name=='nt':
    DEBUG = True
else:
    DEBUG = True
#DEBUG=True

ALLOWED_HOSTS = ['206.189.141.255', 'yuva.net.in','www.yuva.net.in','localhost']
SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    # Add your apps here to enable them
    'landing_page',
    'account',
    'manage_dashboard',
    'vimarsh18',
    'django_cleanup',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',
    'storages',
    #'pwa',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yuvacentral.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'yuvacentral.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.name=='nt':
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'yuvacentral',
	'USER': 'adminyash',
	'PASSWORD': '1234admin',
	'HOST': 'localhost',
	'PORT': '',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'

#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
#MAX_UPLOAD_SIZE = 1048576

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

DEFAULT_FROM_EMAIL = 'YUVA <noreply@yuva.net.in>'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST='smtp.sendgrid.net'
EMAIL_HOST_USER='apikey'
EMAIL_HOST_PASSWORD = sendgrid_apikey
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

LOGIN_URL = 'landing:login'
LOGOUT_REDIRECT_URL = 'landing:login'
LOGIN_REDIRECT_URL='account:profile'

#----------------AWS----------------------------

if os.name!='nt':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

    AWS_ACCESS_KEY_ID = access_id
    AWS_SECRET_ACCESS_KEY = access_key
    AWS_STORAGE_BUCKET_NAME = bucket_name

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    DEFAULT_FILE_STORAGE = 'yuvacentral.storage_backends.MediaStorage' 
    #PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static', 'js', 'serviceworker.js')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
    MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))
    MEDIA_URL = '/media/'
    #PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static', 'js', 'serviceworker.js')

#PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

# PWA_APP_NAME = 'YUVA'
# PWA_APP_DESCRIPTION = "Youth United for Vision and Action"
# PWA_APP_THEME_COLOR = '#f59402'
# PWA_APP_DISPLAY = 'standalone'
# PWA_APP_START_URL = '/'
# PWA_APP_ICONS = [
#     {
#         'src': STATIC_URL+'assets/img/icons/logo512.png',
#         'sizes': '512x512'
#     },
#      {
#         'src': STATIC_URL+'assets/img/icons/favicon-196x196.png',
#         'sizes': '196x196'
#     }
# ]