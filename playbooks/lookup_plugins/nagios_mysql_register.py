import oauth2
import json
import re


class LookupModule(object):
    def __init__(self, *args, **kwargs):
        pass

    def run(self, oauth_key, oauth_secret, nagios_server, inventory, groups, contacts, *args, **kwargs):
        group = re.match('.*/(.*)', inventory).group(1)
        hosts = groups["mysql-db-server"]

        consumer = oauth2.Consumer(key=oauth_key, secret=oauth_secret)
        client = oauth2.Client(consumer)

        try:
            # Create the hostgroup
            value = client.request("%s/api/v1/hostgroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": group, "alias": group}),
                           headers={"Content-Type": "application/json"})

            # Create services
            # active-service is defined in templates/aca-monitor/nagios/common_configuration.cfg
            # Disk check - values are defined in the ansible variable monitored_disk_partitions
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "Disk Check",
                                            "check_command": "check_acamon_remote!disk_check.py"}),
                           headers={"Content-Type": "application/json"})

            # Inode check - values are defined in the ansible variable monitored_disk_partitions
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "Inode Check",
                                            "check_command": "check_acamon_remote!inode_check.py"}),
                           headers={"Content-Type": "application/json"})

            # load average check - values are defined in the ansible variable monitored_load
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "Load Average Check",
                                            "check_command": "check_acamon_remote!load_check.py"}),
                           headers={"Content-Type": "application/json"})

            # cpu idle check - values are defined in the ansible variable monitored_cpu_idle
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "CPU Idle Check",
                                            "check_command": "check_acamon_remote!cpu_idle_check.py"}),
                           headers={"Content-Type": "application/json"})

            # mysql sql connections check
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "MySQL Connections Check",
                                            "check_command": "check_acamon_remote!mysql_connections_check.py"}),
                           headers={"Content-Type": "application/json"})

            # mysql open files check
            value = client.request("%s/api/v1/service" % (nagios_server),
                           method='POST',
                           body=json.dumps({"base_service": "active-service",
                                            "description": "MySQL Open Files Check",
                                            "check_command": "check_acamon_remote!mysql_open_files.py"}),
                           headers={"Content-Type": "application/json"})

            # mysql master check
            value = client.request("%s/api/v1/service" % (nagios_server),
                method='POST',
                body=json.dumps({"base_service": "active-service",
                                 "description": "MySQL Master Check",
                                 "check_command": "check_acamon_remote!mysql_master_check.py"}),
                headers={"Content-Type": "application/json"})

            # mysql slave check
            value = client.request("%s/api/v1/service" % (nagios_server),
                method='POST',
                body=json.dumps({"base_service": "active-service",
                                 "description": "MySQL Slave Check",
                                 "check_command": "check_acamon_remote!mysql_slave_check.py"}),
                headers={"Content-Type": "application/json"})

            # Create disk service group
            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": "Disk Services", "alias": "Disk Services"}),
                           headers={"Content-Type": "application/json"})

            # Create the cpu service group
            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": "CPU Services", "alias": "CPU Services"}),
                           headers={"Content-Type": "application/json"})

            # Create the mysql db service group
            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": "MySQL DB Services", "alias": "MySQL DB Services"}),
                           headers={"Content-Type": "application/json"})

            # Add the services to their groups
            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "Disk Services", "service": "Disk Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "Disk Services", "service": "Inode Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "CPU Services", "service": "CPU Idle Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "CPU Services", "service": "Load Average Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "MySQL DB Services", "service": "MySQL Connections Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "MySQL DB Services", "service": "MySQL Open Files Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "MySQL DB Services", "service": "MySQL Master Check"}),
                                   headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                                   method='PATCH',
                                   body=json.dumps({"group": "MySQL DB Services", "service": "MySQL Slave Check"}),
                                   headers={"Content-Type": "application/json"})

            # Create each hosts
            for host in hosts:
                value = client.request("%s/api/v1/host" % (nagios_server),
                               method='POST',
                               body=json.dumps({"name": host, "address": host, "contact_groups": ""}),
                               headers={"Content-Type": "application/json"})

                # Add the hosts to the hostgroup
                value = client.request("%s/api/v1/hostgroup" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"group": group, "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the disk check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "Disk Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the inode check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "Inode Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the load average check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "Load Average Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the cpu idle check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "CPU Idle Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the connections check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "MySQL Connections Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the open files check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "MySQL Open Files Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

            for host in groups.get("mysql-db-server-master", []):
                # Add the DB master check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "MySQL Master Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

            for host in groups.get("mysql-db-server-slave", []):
                # Add the DB slave check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "MySQL Slave Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

            # Deploy the updated nagios configuration
            value = client.request("%s/api/v1/deploy" % (nagios_server), method="POST")
            return [str(value)]

        except Exception as ex:
            return [str(ex)]

