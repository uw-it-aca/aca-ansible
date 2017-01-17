
SQLSHARE_WEB_HOST = '{{ sqlshare_web_host }}'
SQLSHARE_REST_HOST = '{{ sqlshare_rest_host }}'

SQLSHARE_OAUTH_ID='{{ sqlshare_oauth_id }}'
SQLSHARE_OAUTH_SECRET='{{ sqlshare_oauth_secret }}'

SQLSHARE_FILE_CHUNK_PATH = "/data/sqlshare/uploads/file_chunks"


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

INSTALLED_APPS += (
    'sqlshare_web', 'templatetag_handlebars',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


MIDDLEWARE_CLASSES += (
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
)

from django_mobileesp.detector import mobileesp_agent as agent
DETECT_USER_AGENTS = {
    'is_tablet': agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
