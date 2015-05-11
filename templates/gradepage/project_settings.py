# Settings for GradePage project.
TIME_ZONE = 'America/Los_Angeles'

MIDDLEWARE_CLASSES += (
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
)

INSTALLED_APPS += (
    'django.contrib.humanize',
    'templatetag_handlebars',
    'handlebars_i18n',
    'south',
    'supporttools',
    'restclients',
    'userservice',
    'authz_group',
    'course_grader',
    'grade_conversion_calculator',
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'add_user': {
            '()': 'course_grader.log.UserFilter'
        },
        'info_only': {
            '()': 'course_grader.log.InfoFilter'
        },
    },
    'formatters': {
        'course_grader': {
            'format': '%(asctime)s %(user)s %(actas)s %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S]',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'course_grader': {
            'filters': ['info_only', 'add_user'],
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/course_grader.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365,
            'formatter': 'course_grader',
        },
        'course_grader_errors': {
            'level': 'ERROR',
            'filters': ['add_user'],
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/errors.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 365,
            'formatter': 'course_grader',
        },
        'console': {
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
        'course_grader': {
            'handlers': ['course_grader', 'course_grader_errors'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

GRADEPAGE_ADMIN_GROUP = '{{ support_group }}'

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'
USERSERVICE_VALIDATION_MODULE = 'course_grader.dao.person.is_netid'
USERSERVICE_ADMIN_GROUP = GRADEPAGE_ADMIN_GROUP

RESTCLIENTS_ADMIN_GROUP = GRADEPAGE_ADMIN_GROUP
RESTCLIENTS_TIMEOUT = 60
RESTCLIENTS_DAO_CACHE_CLASS = 'course_grader.cache.RestClientsCache'

ALLOW_GRADE_SUBMISSION_OVERRIDE = {{ allow_grade_submission_override }}

EMAIL_BACKEND = '{{ email_backend }}'
EMAIL_HOST = '{{ email_host }}'
EMAIL_NOREPLY_ADDRESS = 'GradePage <{{ email_noreply_address }}>'
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}

{% for host in allowed_hosts|default([]) %}
GRADEPAGE_HOST = 'https://{{ host }}'
{% endfor %}
SUBMISSION_DEADLINE_WARNING_HOURS = 48
PAST_TERMS_VIEWABLE = 4
GRADE_RETENTION_YEARS = 5

SUPPORTTOOLS_PARENT_APP = 'GradePage'

from django_mobileesp.detector import agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'course_grader.context_processors.user',
    'course_grader.context_processors.has_less_compiled',
    'course_grader.context_processors.debug_mode',
    'supporttools.context_processors.supportools_globals',
)
