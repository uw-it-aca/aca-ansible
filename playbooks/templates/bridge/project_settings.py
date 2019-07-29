INSTALLED_APPS += (
    'rc_django',
    'sis_provisioner.apps.BridgeProvisionerConfig',
)

BRIDGE_IMPORT_CSV_ROOT = '/data/bridge/csv'
BRIDGE_IMPORT_USER_FILE_SIZE = {{ import_user_file_size }}
BRIDGE_USER_WORK_POSITIONS = {{ user_work_positions }}

RESTCLIENTS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
RESTCLIENTS_DISABLE_THREADING = True
RESTCLIENTS_TIMEOUT = 60
TIMING_LOG_ENABLED = True
ERRORS_TO_ABORT_LOADER = [401, 500, 502, 503]
# 502 Bad Gateway
# 503 Service Unavailable
# 504 Gateway Timeout

# RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/data/bridge/cache',
        'OPTIONS': {
            'MAX_ENTRIES': 200000
            }
        }
    }

import sys

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'bridge': {
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
        'bridge': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '/data/bridge/logs/%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'bridge',
        },
        'restclients_timing_log': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '/data/bridge/logs/timing/%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'bridge',
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
   'loggers': {
        'bridge_provisioner_commands': {
            'handlers': ['mail_admins', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'restclients_core': {
            'handlers': ['restclients_timing_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'rc_django': {
            'handlers': ['restclients_timing_log'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['bridge'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
