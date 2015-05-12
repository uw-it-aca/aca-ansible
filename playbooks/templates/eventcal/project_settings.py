# Settings for Event Calendar project.
INSTALLED_APPS += (
    'south',
    'restclients',
    'accountsynchr',
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
        'standard': {
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
        'dailyrotation_file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'accountsynchr.util.dailylogfile.DailyLogFileHandler',
            'filename': '/data/eventcal/logs/acc_synchr',
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
        '': {
            'handlers': ['dailyrotation_file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

EVENTCAL_ADMIN_GROUP = 'u_netid_eventcal_admins'

RESTCLIENTS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
