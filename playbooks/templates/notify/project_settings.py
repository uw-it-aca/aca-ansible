# Settings for Notify project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'templatetag_handlebars',
    'supporttools',
    'userservice',
    'authz_group',
    'notify.apps.NotifyUIConfig',
    'rc_django',
]

MIDDLEWARE_CLASSES += [
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
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
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'event_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/events.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'ui_log': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/ui.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
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
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'notify': {
            'handlers': ['ui_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'notify.events': {
            'handlers': ['event_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
USERSERVICE_VALIDATION_MODULE = 'notify.userservice_validation_module.validate_override_user'
USERSERVICE_ADMIN_GROUP = '{{ support_group }}'
RESTCLIENTS_ADMIN_GROUP = USERSERVICE_ADMIN_GROUP
RESTCLIENTS_DAO_CACHE_CLASS='notify.cache_implementation.UICache'

AWS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
AWS_SQS = {
    'ENROLLMENT_V2': {
        'TOPIC_ARN': '{{ event_enrollment_v2_topic_arn }}',
        'QUEUE': '{{ event_enrollment_v2_sqs_queue }}',
        'KEY_ID': '{{ event_enrollment_v2_key_id }}',
        'KEY': '{{ event_enrollment_v2_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': {{ event_enrollment_v2_sqs_gather }},
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {}
    },
}

SUPPORT_EMAIL = '{{ support_email }}'
SENDER_ADDRESS = '{{ sender_address }}'

{% if google_analytics_key|default(None) %}
GOOGLE_ANALYTICS_KEY = '{{ google_analytics_key }}'
{% endif %}

UI_SYSTEM_MESSAGE = None

SUPPORTTOOLS_PARENT_APP = 'Notify.UW'

from django_mobileesp.detector import mobileesp_agent as agent
DETECT_USER_AGENTS = {
    'is_android': agent.detectAndroid,
    'is_ios': agent.detectIos,
    'is_windows_phone': agent.detectWindowsPhone,
    'is_mobile': agent.detectTierTablet | \
                 agent.detectTierIphone | \
                 agent.detectMobileQuick,
}
