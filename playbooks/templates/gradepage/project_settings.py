# Settings for GradePage project.
TIME_ZONE = 'America/Los_Angeles'

# Explicitly set for Django 1.7 warnings
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Redefines MIDDLEWARE_CLASSES to use custom RemoteUserMiddleware
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'userservice.user.UserServiceMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
]

INSTALLED_APPS += [
    'django.contrib.humanize',
    'templatetag_handlebars',
    'supporttools',
    'restclients',
    'userservice',
    'authz_group',
    'course_grader',
    'grade_conversion_calculator',
]

TEMPLATES[0]['OPTIONS']['context_processors'].extend([
    'course_grader.context_processors.user',
    'course_grader.context_processors.has_less_compiled',
    'course_grader.context_processors.debug_mode',
    'supporttools.context_processors.supportools_globals'
])

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
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/course-grader-%Y-%m-%d',
            'permissions': 0o664,
            'formatter': 'course_grader',
        },
        'course_grader_errors': {
            'level': 'ERROR',
            'filters': ['add_user'],
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/errors-%Y-%m-%d',
            'permissions': 0o664,
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

LOGIN_URL = '/user_login'

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

GRADEPAGE_SUPPORT_EMAIL = '{{ gradepage_support_email }}'
REGISTRAR_SUPPORT_EMAIL = '{{ registrar_support_email }}'
REGISTRAR_SUPPORT_PHONE = '{{ registrar_support_phone }}'

SUPPORTTOOLS_PARENT_APP = 'GradePage'

from django_mobileesp.detector import agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}
