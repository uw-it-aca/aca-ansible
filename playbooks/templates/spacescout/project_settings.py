DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ default_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ default_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ default_db_pass }}',                  # Not used with sqlite3.
        'HOST': '{{ db_hostname }}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.

    },
    'server': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ server_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ server_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ server_db_pass }}',                  # Not used with sqlite3.
        'HOST': '{{ db_hostname }}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'web': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ web_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ web_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ web_db_pass }}',                  # Not used with sqlite3.
        'HOST': '{{ db_hostname }}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'admin': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ admin_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ admin_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ admin_db_pass }}',                  # Not used with sqlite3.
        'HOST': '{{ db_hostname }}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASE_ROUTERS = ['spacescout_util.db_router.LegacyRouter']

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'spacescout_file': {
            'level': 'WARNING',
            'class': 'permissions_logging.DateNameFileHandler',
            'permissions': 0o664,
            'filename': '{{ base_dir }}/logs/spacescout-%Y-%m-%d.log',
            'formatter': 'standard',
        },
        'labstats_file': {
            'level': 'WARNING',
            'class': 'permissions_logging.DateNameFileHandler',
            'permissions': 0o664,
            'filename': '{{ base_dir }}/logs/labstats-%Y-%m-%d.log',
            'formatter': 'standard',
        },

    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'spacescout_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'spacescout_labstats': {
            'handlers': ['mail_admins', 'labstats_file'],
            'level': 'WARNING',
            'propagate': True,
        },

    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/server-cache',
        'TIMEOUT': 60 * 60 * 24,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    }
}

# from the web project's local settings on spotseeker-test
OAUTH_AUTHORIZE_VIEW = 'spotseeker_server.views.oauth.authorize'
OAUTH_CALLBACK_VIEW = 'spotseeker_server.views.oauth.callback'

# Required by spacescout_labstats, as well
SS_WEB_SERVER_HOST = 'http://{{ spacescout_web_app_hostname }}'
# Run ./manage.py create_consumer on the server and copy the key and secret below. You'll also need to go into the admin and make the oauth client "Trusted."
# These two required by spacescout_labstats, as well
SS_WEB_OAUTH_KEY = '{{ spacescout_web_oauth_key }}'
SS_WEB_OAUTH_SECRET = '{{ spacescout_web_oauth_secret }}'

# Enable sending of email
EMAIL_HOST = '{{ email_host }}'
EMAIL_USE_TLS = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # This can be removed when we hit 1.9 and can use PersistentRemoteUserMiddleware
    'spotseeker_server.middleware.persistent.PersistentSessionMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

INSTALLED_APPS += (
    'django.contrib.admin',
    'oauth_provider',
    'spotseeker_server',
    'spacescout_labstats',
)

# From the server project settings:
CACHE_MIDDLEWARE_SECONDS = 60 * 60  # Cache what we can for an hour

# From the server project local settings:

# Values can be one of 'all_ok' or 'oauth'. If using 'oauth', client applications will need an oauth key/secret pair.
SPOTSEEKER_AUTH_MODULE = 'spotseeker_server.auth.oauth'

# Custom validation can be added by adding SpotForm and ExtendedInfoForm to org_forms and setting them here.
SPOTSEEKER_SPOT_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotForm'
SPOTSEEKER_SPOTEXTENDEDINFO_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotExtendedInfoForm'
SPOTSEEKER_SEARCH_FILTERS = ['spotseeker_server.org_filters.uw_search.Filter']

OAUTH_PROVIDER_SECRET_SIZE = 64

JSON_PRETTY_PRINT = False

SPOTSEEKER_AUTH_ADMINS = {{ ss_auth_admins }}

MEDIA_ROOT = '/data/www/media/'
MEDIA_URL = '/media/'

USER_EMAIL_DOMAIN = "{{ email_domain }}"

# LDAP server to search
SS_LDAP_DIRECTORY = '{{ ldap_directory }}'

# LDAP search parameters
SS_LDAP_SEARCH_BASE = '{{ ldap_search_base }}'

{% if labstats_url is defined %}
LABSTATS_URL = '{{ labstats_url }}'
{% endif %}

{% if cte_techloan_url is defined %}
CTE_TECHLOAN_URL = '{{ cte_techloan_url }}'
{% endif %}

LS_CENTER_LAT = '47.655003'
LS_CENTER_LON = '-122.306864'
LS_SEARCH_DISTANCE = '10000'
