# Settings for Bridge project.
# Django 1.9.6.
#import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIME_ZONE = 'America/Los_Angeles'

STATIC_URL = '/data/bridge/static/'

# Assign rather than append since order is significant
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userservice.user.UserServiceMiddleware',
]

INSTALLED_APPS += (
    'restclients',
    'sis_provisioner.apps.Sis_provisionerConfig',
)

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
RESTCLIENTS_ADMIN_GROUP = '{{ restclients_admin_group }}'
# USERSERVICE_ADMIN_GROUP = '{{ userservice_admin_group }}'
# USERSERVICE_VALIDATION_MODULE = ''
# SUPPORTTOOLS_PARENT_APP = "AdminBridge"
# SUPPORTTOOLS_PARENT_APP_URL = "/"

# BRIDGE_ADMIN_GROUP = '{{ bridge_admin_group }}'
BRIDGE_IMPORT_CSV_ROOT='/data/bridge/csv'
BRIDGE_IMPORT_USER_FILENAME='users'
BRIDGE_IMPORT_USER_FILE_SIZE={{ import_user_file_size }}

RESTCLIENTS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
RESTCLIENTS_DAO_CACHE_CLASS='{{restclients_dao_cache_class}}'
RESTCLIENTS_DISABLE_THREADING = True
RESTCLIENTS_TIMEOUT = 60

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/data/bridge/cache',
    }
}

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
        'restclients': {
            'handlers': ['bridge'],
            'level': 'INFO',
            'propagate': True,
        },
        'sis_provisioner': {
            'handlers': ['bridge'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
