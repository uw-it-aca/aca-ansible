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
        'null': {
            'class': 'logging.NullHandler',
        },
        # don't enable until we have permissionslogging set up
        #'spacescout_file': {
        #    'level': 'WARNING',
        #    'class': 'logging.FileHandler',
        #    'filename': '{{ base_dir }}/spacescout.log',
        #    'formatter': 'standard',
        #},
        #'labstats_file': {
        #    'level': 'WARNING',
        #    'class': 'logging.FileHandler',
        #    'filename': '/tmp/test1_labstats.log',
        #    'formatter': 'standard',
        #},

    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        'labstats_spacescout': {
            'handlers': ['mail_admins'],
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
    'spacescout_web.context_processors.show_ios_smart_banner',
    'spacescout_web.context_processors.less_not_compiled',
    'spacescout_web.context_processors.is_mobile',
    'spacescout_web.context_processors.ga_tracking_id',
    'spacescout_web.context_processors.gmaps_api_key',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/server-cache'
    }
}

# from the web project's local settings on spotseeker-test
OAUTH_AUTHORIZE_VIEW = 'spotseeker_server.views.oauth.authorize'
OAUTH_CALLBACK_VIEW = 'spotseeker_server.views.oauth.callback'

MOBILE_USER_AGENTS = 'android|fennec|iemobile|iphone|ipad|opera (?:mini|mobi)'

FEEDBACK_EMAIL_RECIPIENT = ['{{ feedback_email_recip }}']
DEFAULT_FROM_EMAIL = '{{ from_email }}' # If the user doesn't specify an email address when they report a problem
SHOW_IOS_SMART_BANNER = True

# For links back to the web app - sharing a space
SS_APP_SERVER = '{{ spacescout_web_app_hostname }}'

SS_WEB_SERVER_HOST = 'http://{{ spacescout_web_app_hostname }}'
# Run ./manage.py create_consumer on the server and copy the key and secret below. You'll also need to go into the admin and make the oauth client "Trusted."
SS_WEB_OAUTH_KEY = '{{ spacescout_web_oauth_key }}'
SS_WEB_OAUTH_SECRET = '{{ spacescout_web_oauth_secret }}'

SS_WEB_LOGOUT_URL = '/user_logout'

DEFAULT_CENTER_LATITUDE = '47.655003'
DEFAULT_CENTER_LONGITUDE = '-122.306864'

SS_LOCATIONS = {
    'seattle': {
        'NAME': 'UW Seattle',
        'CENTER_LATITUDE': '47.655003',
        'CENTER_LONGITUDE': '-122.306864',
        'ZOOM_LEVEL': '15',
    },
    'tacoma': {
        'NAME': 'UW Tacoma',
        'CENTER_LATITUDE': '47.24579',
        'CENTER_LONGITUDE': '-122.43737',
        'ZOOM_LEVEL': '17',
    },
    'bothell': {
        'NAME': 'UW Bothell',
        'CENTER_LATITUDE': '47.761296',
        'CENTER_LONGITUDE': '-122.193097',
        'ZOOM_LEVEL': '16',
    }
}
SS_DEFAULT_LOCATION = 'seattle'

# This is the list of zoom levels for which the spaces are clustered by building on the map.  An empty list means no building clustering
SS_BUILDING_CLUSTERING_ZOOM_LEVELS = [15, 16, 17]

# The ratio (distance between spaces / diagonal distance visible on map) below which spaces will cluster
# together on the map when not clustering by building
SS_DISTANCE_CLUSTERING_RATIO = .04

# Enable sending of email
EMAIL_HOST = '{{ email_host }}'
EMAIL_USE_TLS = True

# Enable Google Analytics
GA_TRACKING_ID = '{{ google_analytics_id }}'
GMAPS_API_KEY = '{{ google_maps_api_key }}'

MIDDLEWARE_CLASSES = (
    'spacescout_web.middleware.unpatch_vary.UnpatchVaryMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # This can be removed when we hit 1.9 and can use PersistentRemoteUserMiddleware
    'spacescout_web.middleware.persistent.PersistentSessionMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'mobility.middleware.DetectMobileMiddleware',
    'mobility.middleware.XMobileMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)


INSTALLED_APPS += (
    'django.contrib.admin',
    'spacescout_web',
    'compressor',
    'templatetag_handlebars',
    'oauth_provider',
    'spotseeker_server',
    'spacescout_labstats',
)

# From the server project settings:
CACHE_MIDDLEWARE_SECONDS = 60 * 60  # Cache what we can for an hour

INSTALLED_APPS += (
    'south',
)

# From the server project local settings:

# Values can be one of 'all_ok' or 'oauth'. If using 'oauth', client applications will need an oauth key/secret pair.
SPOTSEEKER_AUTH_MODULE = 'spotseeker_server.auth.oauth'
#SPOTSEEKER_AUTH_MODULE = 'spotseeker_server.auth.all_ok'

# Custom validation can be added by adding SpotForm and ExtendedInfoForm to org_forms and setting them here.
SPOTSEEKER_SPOT_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotForm'
SPOTSEEKER_SPOTEXTENDEDINFO_FORM = 'spotseeker_server.org_forms.uw_spot.UWSpotExtendedInfoForm'
SPOTSEEKER_SEARCH_FILTERS = ['spotseeker_server.org_filters.uw_search.Filter']

# Custom filter for the web app
SPACESCOUT_SEARCH_FILTERS = ['spacescout_web.org_filters.uw_search.Filter']

OAUTH_PROVIDER_SECRET_SIZE = 64

# admin project settings.py:
SPACE_TABLE_KEYS = {
    'FIXED': ('id', 'name',),
    'SCROLLABLE': ('type',),
}

INSTALLED_APPS += (
    'django_verbatim',
    'spacescout_admin',
)

# Admin project local_settings.py:
# Email to receive notice of publication requests
SS_PUBLISHER_EMAIL = [
{% for email in admin_publish_emails %}
    '{{ email }}',
{% endfor %}
]

# Email subject of publication requests
SS_PUBLISHER_FROM = '{{ admin_from_email }}'

SS_ADMIN_SERVER_HOST = '{{ admin_app_ss_server }}'
SS_ADMIN_OAUTH_KEY = '{{ admin_app_ss_oauth_key }}'
SS_ADMIN_OAUTH_SECRET = '{{ admin_app_ss_oauth_secret }}'

# Key Used to Describe Spaces
SS_SPACE_DESCRIPTION = 'extended_info.location_description'
SS_ADMIN_FIELDS_MODULE = 'spacescout_admin.field_definitions.uw'

JSON_PRETTY_PRINT = False
APP_URL_ROOT = '/admin/'

SPOTSEEKER_AUTH_ADMINS = {{ ss_auth_admins }}

MEDIA_ROOT = '/data/www/media/'
MEDIA_URL = '/media/'

USER_EMAIL_DOMAIN = "{{ email_domain }}"

# LDAP server to search
SS_LDAP_DIRECTORY = '{{ ldap_directory }}'

# LDAP search parameters
SS_LDAP_SEARCH_BASE = '{{ ldap_search_base }}'

LABSTATS_URL = '{{ labstats_url }}'

LS_CENTER_LAT = '47.655003'
LS_CENTER_LON = '-122.306864'
LS_SEARCH_DISTANCE = '10000'
