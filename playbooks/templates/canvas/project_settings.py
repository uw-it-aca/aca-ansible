# Settings for Canvas project.

STATICFILES_DIRS = (
    '{{ base_dir }}/builds/{{ current_build_value }}/statics',
)

TEMPLATE_DIRS = (
    '{{ base_dir }}/builds/{{ current_build_value }}/templates',
)

TIME_ZONE = 'America/Los_Angeles'

MIDDLEWARE_CLASSES += (
    'blti.middleware.CSRFHeaderMiddleware',
    'blti.middleware.SessionHeaderMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
)

INSTALLED_APPS += (
    'django.contrib.humanize',
    'south',
    'templatetag_handlebars',
    'supporttools',
    'restclients',
    'userservice',
    'authz_group',
    'blti',
    'sis_provisioner',
    'admin',
    'astra',
    'events',
    'course_request',
    'libguide',
    'analytics',
    'grade_conversion_calculator',
    'grading_standard',
    'utils',
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
        'event_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/events.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'astra_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/astra.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'groups_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/groups.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'sis_provisioner_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/sis_provisioner.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'course_request_file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/course_request.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sis_provisioner': {
            'handlers': ['sis_provisioner_file'],
            'level': 'DEBUG'
        },
        'events': {
            'handlers': ['event_file'],
            'level': 'DEBUG'
        },
        'astra': {
            'handlers': ['astra_file'],
            'level': 'DEBUG'
        },
        'groups': {
            'handlers': ['groups_file'],
            'level': 'DEBUG'
        },
        'course_request': {
            'handlers': ['course_request_file'],
            'level': 'DEBUG'
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

ASTRA_ROLE_MAPPING = {
    "accountadmin": "AccountAdmin",
    "tier1support": "UW-IT Support Tier 1",
    "tier2support": "UW-IT Support Tier 2",
    "CollDeptAdminCourseDesign": "College or Dept Admin or Designer",
    "CollDeptSuptOutcomeMgr": "College or Dept Support or Outcomes Manager",
    "CollDeptResearchObserve": "College or Dept Researcher or Observer",
    "UWEOAdmin": "UWEO Admin",
    "UWEOManager": "UWEO Manager",
    "UWEOProgram": "UWEO Program",
    "UWEOOperations": "UWEO Operations",
    "UWEOReadOnly": "UWEO Read Only",
    "APIUserReadOnly": "API User (Read Only)",
    "APIUserReadWrite": "API User (Read-Write)"
}

CANVAS_MASQUERADE_ROLE = "Become users only (dept. admin)"
ANCILLARY_CANVAS_ROLES = {
    "CollDeptAdminCourseDesign": {
        "account": "root",
        "canvas_role": CANVAS_MASQUERADE_ROLE
    },
    "UWEOAdmin": {
        "account": "root",
        "canvas_role": CANVAS_MASQUERADE_ROLE
    },
    "UWEOManager": {
        "account": "root",
        "canvas_role": CANVAS_MASQUERADE_ROLE
    },
    "APIUserReadWrite": {
        "account": "root",
        "canvas_role": CANVAS_MASQUERADE_ROLE
    },
    "APIUserReadOnly": {
        "account": "root",
        "canvas_role": CANVAS_MASQUERADE_ROLE
    },
}

LTI_CONSUMERS = {
{% for consumer in lti_consumers|default([]) %}
    '{{ consumer.key }}': '{{ consumer.secret }}',
{% endfor %}
}

BLTI_AES_KEY = b'{{ blti_aes_key }}'
BLTI_AES_IV = b'{{ blti_aes_iv }}'

SESSION_COOKIE_NAME = 'cvssessionid'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_DOMAIN = '.uw.edu'
CSRF_COOKIE_DOMAIN = '.uw.edu'

UW_GROUP_BLACKLIST = [
    'uw_affiliation_',
    'uw_employee',
    'uw_faculty',
    'uw_staff',
    'uw_student',
    'uw_affiliate',
    'uw_member'
]

DEFAULT_GROUP_SECTION_NAME = 'UW Group members'

LOGIN_DOMAIN_WHITELIST = ['gmail.com', 'google.com', 'googlemail.com']

SIS_IMPORT_ROOT_ACCOUNT_ID = 'uwcourse'
SIS_IMPORT_CSV_ROOT = '{{ base_dir }}/var/csv'
SIS_IMPORT_CSV_DEBUG = {{ sis_import_csv_debug|default(False) }}
SIS_IMPORT_GROUPS = ['uw_student', 'uw_faculty', 'uw_staff']
SIS_IMPORT_IMMEDIATE_COURSE_SOCKET='/data/canvas/var/course_socket'
SIS_IMPORT_LIMIT = {
    'course': {
        'default': 500,
        'high': 200
    },
    'enrollment': {
        'default': 1000,
        'high': 100
    },
    'user': {
        'default': 500,
        'high': 500
    },
    'group': {
        'default': 500
    },
    'coursemember': {
        'default': 1000
    }
}

AUTHZ_GROUP_BACKEND = 'authz_group.authz_implementation.uw_group_service.UWGroupService'

CANVAS_MANAGER_ADMIN_GROUP = 'u_acadev_canvas_support'
RESTCLIENTS_ADMIN_GROUP = 'u_acadev_canvas_support-admin'
USERSERVICE_ADMIN_GROUP = RESTCLIENTS_ADMIN_GROUP

RESTCLIENTS_TIMEOUT = 600
RESTCLIENTS_DISABLE_THREADING = True
RESTCLIENTS_DAO_CACHE_CLASS = 'sis_provisioner.cache.RestClientsCache'
RESTCLIENTS_CANVAS_ACCOUNT_ID = '{{ canvas_account_id }}'
RESTCLIENTS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
SUPPORTTOOLS_PARENT_APP = 'Canvas LMS'
SUPPORTTOOLS_PARENT_APP_URL = RESTCLIENTS_CANVAS_HOST

EVENT_COUNT_PRUNE_AFTER_DAY = 7
EVENT_VALIDATE_SNS_SIGNATURE = True
EVENT_VALIDATE_ENROLLMENT_SIGNATURE = False
EVENT_ENROLLMENT_TOPIC_ARN = '{{ event_enrollment_topic_arn }}'
EVENT_ENROLLMENT_KEYS = {
{% for payload_key in event_enrollment_payload_keys|default([]) %}
    '{{ payload_key.key }}': '{{ payload_key.secret }}',
{% endfor %}
}

AWS_CA_BUNDLE = '{{ base_dir }}/live/lib/python2.6/site-packages/boto/cacerts/cacerts.txt'
EVENT_AWS_SQS_CERT = '{{ webservice_client_cert_path }}'
EVENT_AWS_SQS_KEY = '{{ webservice_client_key_path }}'

EVENT_AWS_ACCESS_KEY_ID = '{{ event_enrollment_key_id }}'
EVENT_AWS_SECRET_ACCESS_KEY = '{{ event_enrollment_secret_key }}'
EVENT_SQS_ENROLLMENT_QUEUE = '{{ event_enrollment_sqs_queue }}'
EVENT_SQS_VISIBILITY_TIMEOUT = 60
EVENT_SQS_MESSAGE_GATHER_SIZE = {{ event_enrollment_sqs_gather }}

AWS_SQS = {
    'ENROLLMENT' : {
        'TOPIC_ARN' : '{{ event_enrollment_topic_arn }}',
        'QUEUE': '{{ event_enrollment_sqs_queue }}',
        'KEY_ID': '{{ event_enrollment_key_id }}',
        'KEY': '{{ event_enrollment_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': {{ event_enrollment_sqs_gather }},
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {
            'KEYS': {
{% for payload_key in event_enrollment_payload_keys|default([]) %}
                '{{ payload_key.key }}': '{{ payload_key.secret }}',
{% endfor %}
            }
        }
    },
    'GROUP' : {
        'TOPIC_ARN' : '{{ event_group_topic_arn }}',
        'QUEUE': '{{ event_group_sqs_queue }}',
        'KEY_ID': '{{ event_group_key_id }}',
        'KEY': '{{ event_group_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': {{ event_group_sqs_gather }},
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {
            'KEYS': {
{% for payload_key in event_group_payload_keys|default([]) %}
                '{{ payload_key.key }}': '{{ payload_key.secret }}',
{% endfor %}
            }
        }
    }
}

LMS_OWNERSHIP_SUBACCOUNT = {
    'PCE_AP': 'uwcourse:uweo:ap-managed',
    'PCE_IELP': 'uwcourse:uweo:ielp-managed',
    'PCE_OL': 'uwcourse:uweo:ol-managed',
    'PCE_NONE': 'uwcourse:uweo:noncredit-campus-managed'
}

ADMIN_EVENT_GRAPH_FREQ = 10
ADMIN_IMPORT_STATUS_FREQ = 30

COURSE_REQUEST_EMAIL_RECIPIENT = '{{ course_request_email_recipient }}'
COURSE_REQUEST_EMAIL_SUBJECT = 'Canvas Course Request'
SANDBOX_SUBACCOUNT_ID = '{{ course_request_sandbox_account }}'
FUTURE_COURSE_ACCOUNT_SIS_SUFFIX = 'future'
FUTURE_COURSE_ACCOUNT_NAME = 'Future Courses'

EMAIL_BACKEND = '{{ email_backend }}'
EMAIL_HOST = '{{ email_host }}'
{% if safe_email_recipient|default(None) %}
SAFE_EMAIL_RECIPIENT = '{{ safe_email_recipient }}'
{% endif %}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'supporttools.context_processors.supportools_globals',
)

from django_mobileesp.detector import agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}
