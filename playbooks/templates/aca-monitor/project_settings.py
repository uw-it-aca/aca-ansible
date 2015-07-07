NAGIOS_CONFIGURATION_FILE = "{{ nagios_configuration_path }}"
NAGIOS_RESTART_COMMAND = "{{ nagios_restart_command }}"


INSTALLED_APPS += (
    'nagios_registration',
    'oauth_provider',
)
