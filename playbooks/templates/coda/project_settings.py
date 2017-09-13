# Settings for Instructor Course Dashboards (coda) project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mobileesp',
    'authz_group',
    'supporttools',
    'compressor',
    'rc_django',
    'templatetag_handlebars',
    'userservice',
    'coursedashboards.apps.CourseDashboardsConfig',
]

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'coda_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/coda.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'sws_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/sws_client.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'gws_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/gws_client.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'pws_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/pws_client.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'sws': {
            'handlers': ['sws_file'],
            'level': 'DEBUG'
        },
        'gws': {
            'handlers': ['gws_file'],
            'level': 'DEBUG'
        },
        'pws': {
            'handlers': ['pws_file'],
            'level': 'DEBUG'
        },
        'coursedashboards': {
            'handlers': ['coda_file'],
            'level': 'DEBUG'
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


USERSERVICE_VALIDATION_MODULE = "coursedashboards.userservice_validation.validate"
USERSERVICE_ADMIN_GROUP='{{ userservice_admin_group }}'
RESTCLIENTS_ADMIN_GROUP='{{ restclients_admin_group }}'
RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'
AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
RESTCLIENTS_MEMCACHED_SERVERS = {{ restclients_memcached_servers|default("''")}}

RESTCLIENTS_DEFAULT_TIMEOUT = 3

SUPPORTTOOLS_PARENT_APP = "CoDa"
SUPPORTTOOLS_PARENT_APP_URL = "/"

from django_mobileesp.detector import mobileesp_agent as agent

MIDDLEWARE_CLASSES += [
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
    'rc_django.middleware.EnableServiceDegradationMiddleware',
]

DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

CODA_ADMIN_GROUP = '{{ coda_admin_group }}'