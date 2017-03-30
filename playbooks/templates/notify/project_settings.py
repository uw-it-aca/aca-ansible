# Settings for Notify project.
TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS += [
    'templatetag_handlebars',
    'supporttools',
    'userservice',
    'authz_group',
    'notify',
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
        'formatter': {
            'format': '%(levelname)-4s %(asctime)s %(message)s [%(name)s] PID:%(process)d',
        },
    },
    'handlers': {
        'can_alerts': {
            'level': 'ERROR',
            'class': 'nws.log.NotificationsLogger',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter'
        },
        'nws_file_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/data/notifications/logs/nws.log',
            'formatter': 'formatter',
        },
        'ui_file_log': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/data/notifications/logs/ui.log',
            'formatter': 'formatter',
        },
    },
    'loggers': {
        'nws': {
            'handlers': ['nws_file_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ui': {
            'handlers': ['ui_file_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
