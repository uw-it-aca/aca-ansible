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

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
USERSERVICE_VALIDATION_MODULE = 'notify.userservice_validation_module.validate_override_user'
USERSERVICE_ADMIN_GROUP = '{{ support_group }}'
RESTCLIENTS_ADMIN_GROUP = USERSERVICE_ADMIN_GROUP

SUPPORT_EMAIL = '{{ support_email }}'
SENDER_ADDRESS = '{{ sender_address }}'

GOOGLE_ANALYTICS_KEY = '{{ google_analytics_key }}'

UI_SYSTEM_MESSAGE = None
