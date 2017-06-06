# Settings for Canvas project.

# Explicitly set for Django 1.7 warnings
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TIME_ZONE = 'America/Los_Angeles'

TEMPLATES[0]['OPTIONS']['context_processors'].extend([
    'supporttools.context_processors.supportools_globals'
])

CACHES = {
    'default' : {
        'BACKEND' : 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION' : 'canvas_sessions'
    }
}

# Assign rather than append since order is significant
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'blti.middleware.CSRFHeaderMiddleware',
    'blti.middleware.SessionHeaderMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.PersistentRemoteUserMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'userservice.user.UserServiceMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
)

INSTALLED_APPS += (
    'django.contrib.humanize',
    'templatetag_handlebars',
    'sis_provisioner.apps.SISProvisionerConfig',
    'supporttools',
    'userservice',
    'authz_group',
    'blti',
    'groups',
    'libguide',
    'course_roster',
    'canvas_users',
    'analytics',
    'grade_conversion_calculator',
    'grading_standard',
    'rc_django',
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
        'event_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/events.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'admin_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/admin.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'astra_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/astra.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'groups_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/groups.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'canvas_users_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/canvas_users.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'grading_standard_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/grading_standard.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7
        },
        'sis_provisioner_log': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/sis_provisioner.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'lti_performance_log': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/lti_performance.log',
            'permissions': 0o664,
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
        },
        'restclients_timing_log': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'permissions_logging.TimedRotatingFileHandler',
            'filename': '{{ base_dir }}/logs/restclients.log',
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
            'handlers': ['sis_provisioner_log'],
            'level': 'DEBUG',
        },
        'sis_provisioner.events': {
            'handlers': ['event_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sis_provisioner.views': {
            'handlers': ['admin_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sis_provisioner.dao.astra': {
            'handlers': ['astra_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'groups': {
            'handlers': ['groups_log'],
            'level': 'DEBUG',
        },
        'canvas_users': {
            'handlers': ['canvas_users_log'],
            'level': 'DEBUG',
        },
        'grading_standard': {
            'handlers': ['grading_standard_log'],
            'level': 'DEBUG',
        },
        'blti.performance': {
            'handlers': ['lti_performance_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'restclients_core.dao': {
            'handlers': ['restclients_timing_log'],
            'level': 'INFO',
            'propagate': False,
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
    "DisabilityResourcesAdm": "Disability Resources Admin",
    "UWEOAdmin": "UWEO Admin",
    "UWEOManager": "UWEO Manager",
    "UWEOProgram": "UWEO Program",
    "UWEOOperations": "UWEO Operations",
    "UWEOReadOnly": "UWEO Read Only",
    "APIUserReadOnly": "API User (Read Only)",
    "APIUserReadWrite": "API User (Read-Write)",
    "AllyApplication": "Ally application"
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
ADD_USER_DOMAIN_WHITELIST = ['uw.edu', 'washington.edu', 'u.washington.edu',
'cac.washington.edu', 'deskmail.washington.edu']

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
NONPERSONAL_NETID_EXCEPTION_GROUP = 'u_acadev_canvas_nonpersonal_netids'

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

AWS_CA_BUNDLE = '{{ base_dir }}/certs/ca-bundle.crt'
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
    'ENROLLMENT_V2': {
        'TOPIC_ARN': '{{ event_enrollment_v2_topic_arn }}',
        'QUEUE': '{{ event_enrollment_v2_sqs_queue }}',
        'KEY_ID': '{{ event_enrollment_v2_key_id }}',
        'KEY': '{{ event_enrollment_v2_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': {{ event_enrollment_v2_sqs_gather }},
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {}
    },
    'INSTRUCTOR_ADD': {
        'TOPIC_ARN': '{{ event_instructor_add_topic_arn }}',
        'QUEUE': '{{ event_instructor_add_sqs_queue }}',
        'KEY_ID': '{{ event_instructor_add_key_id }}',
        'KEY': '{{ event_instructor_add_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': 50,
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {}
    },
    'INSTRUCTOR_DROP': {
        'TOPIC_ARN': '{{ event_instructor_drop_topic_arn }}',
        'QUEUE': '{{ event_instructor_drop_sqs_queue }}',
        'KEY_ID': '{{ event_instructor_drop_key_id }}',
        'KEY': '{{ event_instructor_drop_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': 50,
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {}
    },
    'GROUP': {
        'TOPIC_ARN': '{{ event_group_topic_arn }}',
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
    },
    'PERSON_V1': {
        'TOPIC_ARN': '{{ event_person_change_topic_arn }}',
        'QUEUE': '{{ event_person_change_sqs_queue }}',
        'KEY_ID': '{{ event_person_change_key_id }}',
        'KEY': '{{ event_person_change_secret_key }}',
        'VISIBILITY_TIMEOUT': 60,
        'MESSAGE_GATHER_SIZE': 50,
        'VALIDATE_SNS_SIGNATURE': True,
        'VALIDATE_MSG_SIGNATURE': True,
        'EVENT_COUNT_PRUNE_AFTER_DAY': 2,
        'PAYLOAD_SETTINGS': {}
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

from django_mobileesp.detector import mobileesp_agent as agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}
