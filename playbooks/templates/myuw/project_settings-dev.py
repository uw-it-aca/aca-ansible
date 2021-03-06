# Settings for MyUWMobile project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'userservice',
    'rc_django',
    'supporttools',
    'django_client_logger',
    'blti',
    'hx_toolkit',
    'django_user_agents',
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
        'event': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/event-%Y-%m-%d',
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
        'views_timing': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/view_performance-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'myuw',
        },
        'restclients_timing': {
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
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'restclients_core.dao': {
            'handlers': ['restclients_timing'],
            'level': 'INFO',
            'propagate': False,
        },
        'aws_message': {
            'handlers': ['event'],
            'level': 'INFO',
            'propagate': False,
        },
        'rc_django': {
            'handlers': ['restclients_timing'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.logger.logresp': {
            'handlers': ['views_timing'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.event': {
            'handlers': ['event'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.views.api.banner_message': {
            'handlers': ['pref'],
            'level': 'INFO',
            'propagate': False,
        },
        'myuw.views.logger': {
            'handlers': ['link'],
            'level': 'INFO',
            'propagate': False,
        },
        'card': {
            'handlers': ['card'],
            'level': 'INFO',
            'propagate': False,
        },
        'link': {
            'handlers': ['link'],
            'level': 'INFO',
            'propagate': False,
        },
        'session': {
            'handlers': ['session'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['myuw'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

RESTCLIENTS_MEMCACHED_SERVERS = {{ restclients_memcached_servers|default("''")}}
RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'

TIMING_LOG_ENABLED = True

SUPPORTTOOLS_PARENT_APP = "MyUW"
SUPPORTTOOLS_PARENT_APP_URL = "/"

EMAIL_BACKEND = "{{ email_backend }}"
EMAIL_HOST = "{{ email_host }}"
EMAIL_PORT = {{ email_port }}
EMAIL_TIMEOUT = {{ email_timeout }}
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}

# Assign rather than append since order is significant
MIDDLEWARE += [
    'django_user_agents.middleware.UserAgentMiddleware',
    'rc_django.middleware.EnableServiceDegradationMiddleware',
]

USER_AGENTS_CACHE = None

GOOGLE_ANALYTICS_KEY = "{{ ga_tracker_key }}"
GOOGLE_SEARCH_KEY = '{{ gcse_key }}'

MYUW_DATA_PATH = "{{ base_dir }}"

BLTI_AES_KEY = b'{{ blti_aes_key }}'
BLTI_AES_IV = b'{{ blti_aes_iv }}'

LTI_CONSUMERS = {
{% for consumer in lti_consumers|default([]) %}
    '{{ consumer.key }}': '{{ consumer.secret }}',
{% endfor %}
}

MYUW_PROD_URL = "{{ myuw_prod_url }}"
MYUW_ADMIN_GROUP = "{{ myuw_admin_group }}"
MYUW_OVERRIDE_GROUP = "{{ myuw_override_group }}"
MYUW_ASTRA_GROUP_STEM = "{{ myuw_astra_group_stem }}"
MYUW_TEST_ACCESS_GROUP = "{{ myuw_test_access_group }}"

MYUW_DISABLE_ACTIONS_WHEN_OVERRIDE = {{ myuw_disable_actions_when_override }}

USERSERVICE_VALIDATION_MODULE = "myuw.authorization.validate_netid"
USERSERVICE_OVERRIDE_AUTH_MODULE = "myuw.authorization.can_override_user"
RESTCLIENTS_ADMIN_AUTH_MODULE = "myuw.authorization.can_proxy_restclient"

MYUWCLASS = "{{ myuwclass }}"
REMOTE_USER_FORMAT = "{{ remote_user_format|default("eppn") }}"
MYUW_ENABLED_FEATURES = {{ myuw_enabled_features }}

AWS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'

AWS_SQS = {
    'SECTION_SATSUS_V1': {
        'QUEUE_ARN': '{{ event_section_status_v1_queue_arn }}',
        'KEY_ID': '{{ event_section_status_v1_key_id }}',
        'KEY': '{{ event_section_status_v1_secret_key }}',
        'VISIBILITY_TIMEOUT': 50,
        'MESSAGE_GATHER_SIZE': 10,
        'WAIT_TIME': 5,
        'VALIDATE_SNS_SIGNATURE': True,
        'PAYLOAD_SETTINGS': {}
    }
}

TOKEN_ISSUER = "{{ oidc_token_issuer }}"
TOKEN_AUDIENCE = "{{ oidc_token_audience }}"
TOKEN_LEEWAY = "{{ oidc_token_leeway }}"
