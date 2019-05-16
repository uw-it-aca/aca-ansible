
DEBUG = {{ debug|default(False) }}

{% if not skip_compress_statics|default(False) %}
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = '{{ base_dir }}/static/{{ current_build_value }}'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
{% endif %}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
{% for admin in admins|default([]) %}
    ('{{ admin.name }}', '{{ admin.email }}'),
{% endfor %}
)

MANAGERS = ADMINS

{% if not skip_central_db_config|default(False) %}
DATABASES = {
    'default': {
        'ENGINE': '{{ database_backend|default("django.db.backends.mysql") }}',
        'NAME': '{{ database_name }}',
        'USER': '{{ database_user }}',
        'PASSWORD': '{{ database_password|default("") }}',
        'HOST': '{{ database_host }}',
        'PORT': '{{ database_port|default("") }}',
        'OPTIONS': {
{% for key, value in (database_options|default({})).items() %}
    '{{ key }}': '{{ value }}',
{% endfor %}
        },
    }
}
{% endif %}


ALLOWED_HOSTS = {% if django_version is version_compare('2', '>=') %}[{% else %}({% endif %}

{% for host in allowed_hosts|default([]) %}
    '{{ host }}',
{% endfor %}
{% if django_version is version_compare('2', '>=') %}]{% else %}){% endif %}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '{{ base_dir }}/static/{{ current_build_value }}'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
{% if aca_cdn_path | default(false) %}
STATIC_URL = 'https://aca-cdn.uw.edu/cdn/{{ aca_cdn_path }}/{{ current_build_value }}/'
{% else %}
STATIC_URL = '/static/{{ current_build_value }}/'
{% endif %}


# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = {% if django_version is version_compare('1.9', '>=') %}[{% else %}({% endif %}

    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    {% if not skip_compress_statics|default(False) %}'compressor',{% endif %}

    {% if preprocess_templates|default(False)%}'template_preprocess',{% endif %}

    {% if django_version is version_compare('1.9', '<') %}'null_command',{% endif %}

{% if django_version is version_compare('1.9', '>=') %}]{% else %}){% endif %}


{% if django_version is version_compare('2', '>=') %}MIDDLEWARE{% else %}MIDDLEWARE_CLASSES{% endif %} = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    {% if persistent_remote_user|default(False) %}'django.contrib.auth.middleware.PersistentRemoteUserMiddleware'{% else %}'django.contrib.auth.middleware.RemoteUserMiddleware'{% endif %},

    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    {% if include_userservice|default(True) %}'userservice.user.UserServiceMiddleware',{% endif %}
]


AUTHENTICATION_BACKENDS = {% if django_version is version_compare('1.9', '>=') %}[{% else %}({% endif %}

    '{{ authentication_backend|default('django.contrib.auth.backends.RemoteUserBackend')}}',
{% if django_version is version_compare('1.9', '>=') %}]{% else %}){% endif %}


{% if preprocess_templates|default(False) %}
COMPILED_TEMPLATE_PATH = '{{ base_dir }}/compiled_templates/{{ current_build_value }}'
{% endif %}

{% if django_version is version_compare('1.9', '>=') %}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            {% if preprocess_templates|default(False) %}COMPILED_TEMPLATE_PATH{% endif %}
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                {% if include_supporttools|default(False) %}'supporttools.context_processors.supportools_globals',
                'supporttools.context_processors.has_less_compiled',
                {% endif %}
                {% for context_proc in extra_context_processors|default([]) %}
                '{{ context_proc }}',
                {% endfor %}
            ],
            'loaders': [
                {% if debug|default(False) %}
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                {% else %}
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
                {% endif %}
            ],
            'debug': DEBUG,
        },
    },
]

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static"
    # Don't forget to use absolute paths, not relative paths.
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    {% if not skip_compress_statics|default(False) %}'compressor.finders.CompressorFinder',{% endif %}
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

{% if login_url|default(None) %}
LOGIN_URL = '{{ login_url }}'
{% endif %}

{% else %}

TEMPLATE_DEBUG = DEBUG

AUTHENTICATION_BACKENDS = (
    '{{ authentication_backend|default('django.contrib.auth.backends.RemoteUserBackend')}}',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static"
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    {% if not skip_compress_statics|default(False) %}'compressor.finders.CompressorFinder',{% endif %}
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # Don't forget to use absolute paths, not relative paths.
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

{% endif %}

{% for key, value in restclients|default({})|dictsort %}
{% for client in value %}

{% include "templates/restclients/%s.tmpl"|format(client) %}

{% endfor %}
{% endfor %}

{% if include_python_saml|default(False) %}
{% include "templates/python_saml/project_settings.py" %}
{% endif %}

{% if project_settings_template|default(None) %}
{% include project_settings_template %}
{% endif %}
