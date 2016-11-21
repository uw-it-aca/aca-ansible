GOOGLE_OAUTH_KEY = '{{ google_oauth_key }}'
GOOGLE_OAUTH_SECRET = '{{ google_oauth_secret }}'

GOOGLE_RETURN_URL = '{{ google_return_url }}'
SCOPE = 'https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/userinfo.email'


DATABASES = {
    'default': {
        'ENGINE': 'django_pyodbc',
        'NAME': '{{ database_name }}',
        'USER': '{{ database_user }}',
        'PASSWORD': '{{ database_password }}',
        'OPTIONS': {
            'dsn': '{{ odbc_dsn_name }}',
            'autocommit': True,
            'extra_params': 'TDS_Version=8.0;PORT=1433',
            # This allows us to syncdb...
            'limit_table_list': True,
        }
    }
}

INSTALLED_APPS += (
    'sqlshare_rest',
    'oauth2_provider',
    'authz_group',
    'userservice',
    'supporttools',
    'templatetag_handlebars',
)

USERSERVICE_ADMIN_GROUP = 'sqlshare_support'
AUTHZ_GROUP_BACKEND='authz_group.authz_implementation.settings.Settings'

AUTHZ_GROUP_MEMBERS = { "sqlshare_support": [ {% for username in sqlshare_support_users|default([]) %}"{{ username }}", {% endfor %} ] }


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
        'sqlshare_log': {
            'level': 'INFO',
            'class': 'permissions_logging.DateNameFileHandler',
            'filename': '{{ base_dir }}/logs/sqlshare-rest-%Y-%m-%d',
            'permissions': 0o664,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'sqlshare_rest': {
            'handlers': ['sqlshare_log'],
            'level': 'INFO',
        },
    },
}

MEDIA_ROOT = "/data/sqlshare/user_uploads/"

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

from oauth2_provider.settings import oauth2_settings
oauth2_settings.ALLOWED_REDIRECT_URI_SCHEMES = ['oob', 'http', 'https']

EMAIL_HOST = 'appsubmit.cac.washington.edu'
SQLSHARE_WEB_URL = '{{ sqlshare_web_url }}'
SQLSHARE_SHARING_URL_FORMAT = '{{ sqlshare_sharing_url_format }}'
SQLSHARE_DETAIL_URL_FORMAT = '{{ sqlshare_detail_url_format }}'

