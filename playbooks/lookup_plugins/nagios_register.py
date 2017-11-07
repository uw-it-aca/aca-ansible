import oauth2
import json
import re
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def _create_service(self, description, command):
	# active-service is defined in templates/aca-monitor/nagios/common_configuration.cfg
        return self._request('POST', '/api/v1/service', {
            'base_service': 'active-service',
            'description': description,
            'check_command': command})

    def _create_host(self, host):
        return self._request('POST', '/api/v1/host', {
            'name': host, 'address': host, 'contact_groups': ''})

    def _create_servicegroup(self, name):
        return self._request('POST', '/api/v1/servicegroup', {
	    'name': name, 'alias': name})

    def _create_hostgroup(self, name):
        return self._request('POST', '/api/v1/hostgroup', {
            'name': name, 'alias': name})

    def _add_service_to_group(self, service, group):
        return self._request('PATCH', '/api/v1/servicegroup', {
            'group': group, 'service': service})

    def _add_host_to_group(self, host, group):
        return self._request('PATCH', '/api/v1/hostgroup', {
            'group': group, 'host': host})

    def _add_service_to_host(self, service, host):
        return self._request('PATCH', '/api/v1/service', {
            'service': service, 'host': host})

    def _request(self, method, url, body={}):
        return self._client.request(
            "%s%s" % (self._nagios_server, url),
            method=method,
            body=json.dumps(body),
            headers={"Content-Type": "application/json"})

    def _create_services_and_groups(self):
        # This method does two things:
        # 1. Ensures that services and service groups exist on the nagios host
        # 2. Returns a list of services that are relevant to this host
	services = ["Disk Check", "Inode Check", "Load Average Check", "CPU Idle Check"]

        # Create service groups
        self._create_servicegroup("Disk Services")
        self._create_servicegroup("CPU Services")
        self._create_servicegroup("Process Services")
        self._create_servicegroup("Integrity Services")
        self._create_servicegroup("MySQL DB Services")

        # Disk check values are defined in the ansible variable monitored_disk_partitions
	self._create_service("Disk Check",
			     "check_acamon_remote!disk_check.py")
        self._add_service_to_group("Disk Check", "Disk Services")

	# Inode check values are defined in the ansible variable monitored_disk_partitions
	self._create_service("Inode Check",
			     "check_acamon_remote!inode_check.py")
        self._add_service_to_group("Inode Check", "Disk Services")

	# load average check values are defined in the ansible variable monitored_load
	self._create_service("Load Average Check",
			     "check_acamon_remote!load_check.py")
        self._add_service_to_group("CPU Idle Check", "CPU Services")

	# cpu idle check values are defined in the ansible variable monitored_cpu_idle
	self._create_service("CPU Idle Check",
			     "check_acamon_remote!cpu_idle_check.py")
        self._add_service_to_group("Load Average Check", "CPU Services")

        if "mysql-db-server" in self._current_groups:
	    # mysql sql connections check
	    self._create_service("MySQL Connections Check",
				 "check_acamon_remote!mysql_connections_check.py")
            self._add_service_to_group("MySQL Connections Check", "MySQL DB Services")
            services.append("MySQL Connections Check")

	    # mysql open files check
	    self._create_service("MySQL Open Files Check",
				 "check_acamon_remote!mysql_open_files.py")
            self._add_service_to_group("MySQL Open Files Check", "MySQL DB Services")
            services.append("MySQL Open Files Check")

            if "mysql-db-server-master" in self._current_groups:
		# mysql master check
		self._create_service("MySQL Master Check",
				     "check_acamon_remote!mysql_master_check.py")
                self._add_service_to_group("MySQL Master Check", "MySQL DB Services")
                services.append("MySQL Master Check")

            if "mysql-db-server-slave" in self._current_groups:
		# mysql slave check
		self._create_service("MySQL Slave Check",
				     "check_acamon_remote!mysql_slave_check.py")
                self._add_service_to_group("MySQL Slave Check", "MySQL DB Services")
                services.append("MySQL Slave Check")

            if self._monitored_mailqueue:
                self._create_service("Mailqueue Check",
                                     "check_acamon_remote!mailqueue_check.py")
                self._add_service_to_group("Mailqueue Check", "MySQL DB Services")
                services.append("Mailqueue Check")

	# process checks values are defined in the ansible variable monitored_processes
	for process in self._monitored_processes:
            name = "Process Check (%s)" % process
	    self._create_service(name,
				 "check_acamon_remote!process_check.py!%s" % process)
	    self._add_service_to_group(name, "Process Services")
            services.append(name)

        if self._monitored_svn_path:
            self._create_service("SVN Local Mods",
                                 "check_acamon_remote!svn_local_mods_check.py")
            self._add_service_to_group("SVN Local Mods", "Integrity Services")
            services.append("SVN Local Mods")

        if self._monitored_crontab_path:
            self._create_service("Crontab Check",
                                 "check_acamon_remote!crontab_check.py")
            self._add_service_to_group("Crontab Check", "Integrity Services")
            services.append("Crontab Check")

        return services

    def run(self, values, variables, **kwargs):
        inventory = variables['inventory_file']
        contacts = variables['nagios_contacts']
        hostgroup = re.match('.*/(.*)', inventory).group(1)
        host = variables['inventory_hostname']

        consumer = oauth2.Consumer(
            key=variables['nagios_registration_oauth_key'],
            secret=variables['nagios_registration_oauth_secret'])
        self._client = oauth2.Client(consumer)
        self._nagios_server = variables['nagios_registration_server']

        self._current_groups = variables['group_names']
        self._monitored_processes = variables.get('monitored_processes', [])
        self._monitored_svn_path = variables.get('monitored_svn_path', None)
        self._monitored_mailqueue = variables.get('monitored_mailqueue', False)
        self._monitored_crontab_path = variables.get('monitored_crontab_path', None)

        try:
# Commenting this out while figuring out better options.  Contacts set on the host don't get service alerts
# for the host, and i don't want to create a different entry for each host/service combo.
#            contact_group_name = "cg_%s" % group
#            # Create a contactgroup
#            value = client.request("%s/api/v1/contactgroup" % (nagios_server),
#                           method='POST',
#                           body=json.dumps({"name": contact_group_name}),
#                           headers={"Content-Type": "application/json"})
#
#            # Create the contacts, and add them to the contact group
#            for contact in contacts:
#                value = client.request("%s/api/v1/contact" % (nagios_server),
#                               method='POST',
#                               body=json.dumps({"name": contact["name"], "email": contact["email"]}),
#                               headers={"Content-Type": "application/json"})
#
#                value = client.request("%s/api/v1/contactgroup" % (nagios_server),
#                               method='PATCH',
#                               body=json.dumps({"group": contact_group_name, "contact": contact["name"]}),
#                               headers={"Content-Type": "application/json"})
#

            # Create services
            services = self._create_services_and_groups()

            # Create the hostgroup
            self._create_hostgroup(hostgroup)

            # Create the host
            self._create_host(host)

            # Add the host to the hostgroup
            self._add_host_to_group(host, hostgroup)

            # Add the services to this host
            for service in services:
                self._add_service_to_host(service, host)

            # Deploy the updated nagios configuration
            value = self._request("POST", "/api/v1/deploy")
            return [str(value)]
        except Exception as ex:
            return [str(ex)]

        return ["ok"]
