# Settings for MyUWMobile project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'authz_group',
    'templatetag_handlebars',
    'rc_django',
    'userservice',
    'django_mobileesp',
    'supporttools',
    'django_client_logger',
    'myuw.apps.MyUWConfig',
]

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'myuw': {
            'format': '%(levelname)-4s %(asctime)s %(message)s [%(name)s]',
            'datefmt': '%d %H:%M:%S',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'myuw': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/myuw-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'card': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/card-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'link': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/link-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'session': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/session-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'performance_log': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/view_performance-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'restclients_timing_log': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '/data/myuw/logs/restclients_timing-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },

        'console':{
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
        'restclients_core.dao': {
            'handlers': ['restclients_timing_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.util.performance': {
            'handlers': ['performance_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw': {
            'handlers': ['myuw'],
            'level': 'INFO',
            'propagate': True,
        },
        'card': {
            'handlers': ['card'],
            'level': 'INFO',
            'propagate': True,
        },
        'link': {
            'handlers': ['link'],
            'level': 'INFO',
            'propagate': True,
        },
        'session': {
            'handlers': ['session'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


USERSERVICE_VALIDATION_MODULE = "myuw.userservice_validation.validate"
USERSERVICE_ADMIN_GROUP='{{ userservice_admin_group }}'
RESTCLIENTS_ADMIN_GROUP='{{ restclients_admin_group }}'
RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'
AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
RESTCLIENTS_MEMCACHED_SERVERS = {{ restclients_memcached_servers|default("''")}}

RESTCLIENTS_DEFAULT_TIMEOUT = 3

SUPPORTTOOLS_PARENT_APP = "MyUW"
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

GOOGLE_ANALYTICS_KEY = "{{ ga_tracker_key }}"
GOOGLE_SEARCH_KEY = '{{ gcse_key }}'

{% if myuw_fyp_redirects|default(False) %}
MYUW_USER_SERVLET_URL = "{{ myuw_legacy_url }}"
MYUW_MANDATORY_SWITCH_PATH = "{{ myuw_fyp_list_path }}"
MYUW_OPTIN_SWITCH_PATH = "{{ myuw_optin_list_path }}"
{% endif %}

SERU_LIST = "{{ myuw_seru_path }}"

MYUW_ADMIN_GROUP = '{{ myuw_admin_group }}'
