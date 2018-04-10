# Settings for Provision Request Tool project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'templatetag_handlebars',
    'authz_group',
    'django_mobileesp',
    'rc_django',
    'endorsement',
    'userservice',
    'django_client_logger',
    'supporttools',
]

COMPRESS_PRECOMPILERS += (
    ('text/x-sass', 'pyscss {infile} > {outfile}'),
    ('text/x-scss', 'pyscss {infile} > {outfile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
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
        'endorsement_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/endorsement.log',
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
        'gws': {
            'handlers': ['gws_file'],
            'level': '{{logger_level|default("DEBUG")}}'
        },
        'pws': {
            'handlers': ['pws_file'],
            'level': '{{logger_level|default("DEBUG")}}'
        },
        'endorsement': {
            'handlers': ['endorsement_file'],
            'level': '{{logger_level|default("DEBUG")}}'
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

SUPPORTTOOLS_PARENT_APP = "Provision"
SUPPORTTOOLS_PARENT_APP_URL = "/"

from django_mobileesp.detector import mobileesp_agent as agent

MIDDLEWARE_CLASSES += [
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
]

DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

PROVISION_ADMIN_GROUP = '{{ provision_admin_group }}'
USERSERVICE_ADMIN_GROUP = '{{ provision_admin_group }}'
RESTCLIENTS_ADMIN_GROUP = '{{ provision_admin_group }}'

EMAIL_BACKEND = '{{ email_backend }}'
EMAIL_HOST = '{{ email_host }}'
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}
