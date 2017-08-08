TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'r_pass.apps.RPassConfig',
    'authz_group',
    'rc_django',
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
        'rpass_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/rpass.log',
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
        'r_pass': {
            'handlers': ['rpass_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
RESTCLIENTS_DAO_CACHE_CLASS='r_pass.cache.RPassCache'

FERNET_KEYS = [
{% for field_key in field_keys|default([]) %}
    '{{ field_key }}',
{% endfor %}
]
