NAGIOS_CONFIGURATION_FILE = "{{ nagios_configuration_path }}"
NAGIOS_RESTART_COMMAND = "{{ nagios_restart_command }}"
NAGIOS_ADMIN_GROUP = "{{ nagios_admin_group }}"

INSTALLED_APPS += (
    'nagios_registration',
    'oauth_provider',
    'templatetag_handlebars',
    'uw_saml',
)
