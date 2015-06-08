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
        }
    }
}

INSTALLED_APPS += (
    'sqlshare_rest',
    'oauth2_provider',
)
