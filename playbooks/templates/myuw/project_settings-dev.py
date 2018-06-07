# Settings for MyUWMobile project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += (
    'templatetag_handlebars',
    'rc_django',
    'userservice',
    'supporttools',
    'django_client_logger',
    'myuw.apps.MyUWConfig',
    'blti',
    'django_mobileesp'
)

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
        'pref': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/pref-%Y-%m-%d',
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
        'rc_django': {
            'handlers': ['restclients_timing_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.util.performance': {
            'handlers': ['performance_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.views.choose': {
            'handlers': ['pref'],
            'level': 'INFO',
            'propagate': True,
        },
        'myuw.views.logger': {
            'handlers': ['link'],
            'level': 'INFO',
            'propagate': True,
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

RESTCLIENTS_MEMCACHED_SERVERS = {{ restclients_memcached_servers|default("''")}}
RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'

SUPPORTTOOLS_PARENT_APP = "MyUW"
SUPPORTTOOLS_PARENT_APP_URL = "/"

EMAIL_BACKEND = "{{ email_backend }}"
EMAIL_HOST = "{{ email_host }}"
EMAIL_PORT = {{ email_port }}
EMAIL_TIMEOUT = {{ email_timeout }}
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}

{% if myuw_fyp_redirects|default(False) %}
MYUW_USER_SERVLET_URL = "{{ myuw_legacy_url }}"
MYUW_MANDATORY_SWITCH_PATH = "{{ myuw_fyp_list_path }}"
MYUW_OPTIN_SWITCH_PATH = "{{ myuw_optin_list_path }}"
{% endif %}

# Assign rather than append since order is significant
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'blti.middleware.CSRFHeaderMiddleware',
    'blti.middleware.SessionHeaderMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'userservice.user.UserServiceMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
    'rc_django.middleware.EnableServiceDegradationMiddleware',
)

from django_mobileesp.detector import mobileesp_agent as agent

DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

GOOGLE_ANALYTICS_KEY = "{{ ga_tracker_key }}"
GOOGLE_SEARCH_KEY = '{{ gcse_key }}'

SERU_LIST = "{{ myuw_seru_path }}"

BLTI_AES_KEY = b'{{ blti_aes_key }}'
BLTI_AES_IV = b'{{ blti_aes_iv }}'

LTI_CONSUMERS = {
{% for consumer in lti_consumers|default([]) %}
    '{{ consumer.key }}': '{{ consumer.secret }}',
{% endfor %}
}

MYUW_ADMIN_GROUP = "{{ myuw_admin_group }}"
MYUW_OVERRIDE_GROUP = "{{ myuw_override_group }}"
MYUW_ASTRA_GROUP_STEM = "{{ myuw_astra_group_stem }}"
MYUW_DISABLE_ACTIONS_WHEN_OVERRIDE = "{{ myuw_disable_actions_when_override }}"

USERSERVICE_VALIDATION_MODULE = "myuw.authorization.validate_netid"
USERSERVICE_OVERRIDE_AUTH_MODULE = "myuw.authorization.can_override_user"
RESTCLIENTS_ADMIN_AUTH_MODULE = "myuw.authorization.can_proxy_restclient"

MYUWCLASS = "{{ myuwclass }}"
REMOTE_USER_FORMAT = "{{ remote_user_format|default("eppn") }}"
LOGOUT_URL = "{{ logout_url|default("/user_logout") }}"

MYUW_ENABLED_FEATURES = {{ myuw_enabled_features }}

MYUW_ADMIN_GROUP = "{{ myuw_admin_group }}"
MYUW_OVERRIDE_GROUP = "{{ myuw_override_group }}"
MYUW_ASTRA_GROUP_STEM = "{{ myuw_astra_group_stem }}"
MYUW_DISABLE_ACTIONS_WHEN_OVERRIDE = "{{ myuw_disable_actions_when_override }}"
USERSERVICE_VALIDATION_MODULE = "myuw.authorization.validate_netid"
USERSERVICE_OVERRIDE_AUTH_MODULE = "myuw.authorization.can_override_user"
RESTCLIENTS_ADMIN_AUTH_MODULE = "myuw.authorization.can_proxy_restclient"
