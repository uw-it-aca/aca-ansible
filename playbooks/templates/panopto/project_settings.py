# Settings for Panopto project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += (
    'django.contrib.humanize',
    'templatetag_handlebars',
    'supporttools',
    'rc_django',
    'userservice',
    'authz_group',
    'scheduler',
    'blti',
)

middleware = list(MIDDLEWARE_CLASSES)
middleware.insert(1, 'blti.middleware.SessionHeaderMiddleware')
middleware.insert(1, 'blti.middleware.CSRFHeaderMiddleware')
middleware.append('django_mobileesp.middleware.UserAgentDetectionMiddleware')
MIDDLEWARE_CLASSES = tuple(middleware)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'add_user': {
            '()': 'scheduler.log.UserFilter'
        },
        'info_only': {
            '()': 'scheduler.log.InfoFilter'
        },
    },
    'formatters': {
        'scheduler': {
            'format': '%(asctime)s %(user)s %(actas)s %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S]',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'client_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/api.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365
        },
        'personal_folder_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/personal_folder.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365
        },
        'scheduler': {
            'filters': ['info_only', 'add_user'],
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/scheduler.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365,
            'formatter': 'scheduler',
        },
        'scheduler_errors': {
            'level': 'ERROR',
            'filters': ['add_user'],
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/scheduler_errors.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365,
            'formatter': 'scheduler',
        },
        'audit': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.FileHandler',
            'filename': '{{ base_dir }}/logs/audit.log',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'scheduler': {
            'handlers': ['scheduler', 'scheduler_errors'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'suds.client': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'suds.resolver': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'suds.transport': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'suds.xsd.schema': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'suds.wsdl': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'client': {
            'handlers': ['client_file'],
            'level': 'DEBUG'
        },
        'personal_folder': {
            'handlers': ['personal_folder_file'],
            'level': 'DEBUG'
        },
        'audit': {
            'handlers': ['audit'],
            'level': 'INFO',
        }
    }
}

PANOPTO_ADMIN_GROUP = 'u_acadev_panopto_support'

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
USERSERVICE_ADMIN_GROUP = PANOPTO_ADMIN_GROUP

RESTCLIENTS_ADMIN_GROUP = PANOPTO_ADMIN_GROUP
RESTCLIENTS_TIMEOUT = 60
RESTCLIENTS_DAO_CACHE_CLASS = 'scheduler.cache.RestClientsCache'

SUPPORTTOOLS_PARENT_APP = 'Panopto'
SUPPORTTOOLS_PARENT_APP_URL = 'https://panopto.uw.edu/'

# panopto personal folder
PANOPTO_PERSONAL_FOLDER_NAME_FORMAT = "%s Folder"
PANOPTO_PERSONAL_FOLDER_ID_FORMAT = "personal-folder-%s"
PANOPTO_PERSONAL_FOLDER_DESCRIPTION_FORMAT = "%s Personal Recordings"
PANOPTO_ID_PROVIDER_PREFIXES = ['UWNetid', 'TestCanvas']

# panopto API access details
PANOPTO_API_USER = '{{ panopto_api_user }}'
PANOPTO_API_APP_ID = '{{ panopto_api_app_id }}'
PANOPTO_API_TOKEN = '{{ panopto_api_token }}'
PANOPTO_SERVER = '{{ panopto_api_server }}'

from django_mobileesp.detector import mobileesp_agent as agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'scheduler.context_processors.user',
    'scheduler.context_processors.has_less_compiled',
    'scheduler.context_processors.debug_mode',
    'supporttools.context_processors.supportools_globals',
)

LTI_CONSUMERS = {
{% for consumer in lti_consumers|default([]) %}
    '{{ consumer.key }}': '{{ consumer.secret }}',
{% endfor %}
}

# BLTI session object encryption values
BLTI_AES_KEY = b'{{ blti_aes_key }}'
BLTI_AES_IV = b'{{ blti_aes_iv }}'
