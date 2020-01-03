# Settings for Notify project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'notify.apps.NotifyUIConfig',
    'supporttools',
    'userservice',
    'persistent_message',
    'rc_django',
    'django_user_agents',
]

CACHES = {
    'default' : {
        'BACKEND' : 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION' : 'notify_sessions'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'add_user': {
            '()': 'notify.log.UserFilter'
        }
    },
    'formatters': {
        'ui': {
            'format': '%(asctime)s %(user)s %(actas)s %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S]',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
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
            'level': 'DEBUG',
            'filters': ['add_user'],
            'formatter': 'ui',
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

NOTIFY_ADMIN_GROUP = '{{ support_group }}'
USERSERVICE_VALIDATION_MODULE = 'notify.utilities.validate_override_user'
USERSERVICE_OVERRIDE_AUTH_MODULE = 'notify.views.can_override_user'
RESTCLIENTS_ADMIN_AUTH_MODULE = 'notify.views.can_proxy_restclient'
RESTCLIENTS_DAO_CACHE_CLASS='notify.cache_implementation.UICache'

AWS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
AWS_SQS = {
    'ENROLLMENT_V2': {
        'QUEUE_ARN': '{{ event_enrollment_v2_sqs_queue }}',
        'KEY_ID': '{{ event_enrollment_v2_key_id }}',
        'KEY': '{{ event_enrollment_v2_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': 50,
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_BODY_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
    },
}

EMAIL_BACKEND = '{{ email_backend }}'
EMAIL_HOST = '{{ email_host }}'
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}

SUPPORT_EMAIL = '{{ support_email }}'
SENDER_ADDRESS = '{{ sender_address }}'

{% if google_analytics_key|default(None) %}
GOOGLE_ANALYTICS_KEY = '{{ google_analytics_key }}'
{% endif %}

SUPPORTTOOLS_PARENT_APP = 'Notify.UW'

INVALID_UUIDS = [
    '00000000-0000-0000-0000-000000000000'
]
