"""
Django settings for scoutproject project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

#INTERNAL_IPS = (
#    '127.0.0.1',
#    '0.0.0.0', #add your server's ip address!
#)

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += (
    'django.contrib.admin',
    'scout',
    #'scout_manager',
    'hybridize',
    'turbolinks',
    'spotseeker_restclient',
)

MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

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
                'scout.context_processors.google_analytics',
                'scout.context_processors.is_desktop',
                'scout.context_processors.is_hybrid',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = '/tmp/'
#
# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#     "compressor.finders.CompressorFinder",
# )
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# django mobileesp

from django_mobileesp.detector import mobileesp_agent as agent

DETECT_USER_AGENTS = {

    'is_tablet' : agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,

    'is_and': agent.detectAndroid,
    'is_ios': agent.detectIos,
    'is_win': agent.detectWindowsPhone,
}

COMPRESS_ROOT = "/tmp/"
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'django_pyscss.compressor.DjangoScssFilter'),
    ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = ''
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# google analytics tracking
#GOOGLE_ANALYTICS_KEY = "UA-XXXXXXXX-X"

# htmlmin
HTML_MINIFY = True
