

# Settings for Event Calendar project.
INSTALLED_APPS += [
    'accountsynchr.apps.EventCalConfig',
]

import sys

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
        'standard': {
            'format': '%(levelname)-4s %(asctime)s %(message)s [%(name)s]',
            'datefmt': '%d %H:%M:%S',
        },
    },
    'handlers': {
        'dailyrotation_file': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/acc_synchr.%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'standard',
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'eventcal.commands': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['dailyrotation_file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

EVENTCAL_ADMIN_GROUP = '{{ eventcal_admin_group }}'
CSV_FILE_PATH = '/data/eventcal/csv'

EMAIL_BACKEND = '{{ email_backend}}'
EMAIL_HOST = '{{ email_host }}'
EMAIL_PORT = {{ email_port }}
EMAIL_TIMEOUT = 15
EMAIL_ADDRESS_DOMAIN = '{{ email_address_domain }}'
