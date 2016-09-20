import oauth2
import json
import re
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, values, *args, **kwargs):
        oauth_key = values[0]
        oauth_secret = values[1]
        nagios_server = values[2]
        inventory = values[3]
        groups = values[4]
        contacts = values[5]
        group = re.match('.*/(.*)', inventory).group(1)
        hosts = groups[group]

        consumer = oauth2.Consumer(key=oauth_key, secret=oauth_secret)
        client = oauth2.Client(consumer)

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
#                # Add the hosts to the hostgroup
#                value = client.request("%s/api/v1/contactgroup" % (nagios_server),
#                               method='PATCH',
#                               body=json.dumps({"group": contact_group_name, "contact": contact["name"]}),
#                               headers={"Content-Type": "application/json"})
#

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


            # Create disk service group
            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": "Disk Services", "alias": "Disk Services"}),
                           headers={"Content-Type": "application/json"})

            value = client.request("%s/api/v1/servicegroup" % (nagios_server),
                           method='POST',
                           body=json.dumps({"name": "CPU Services", "alias": "CPU Services"}),
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

            # Deploy the updated nagios configuration
            value = client.request("%s/api/v1/deploy" % (nagios_server), method="POST")
            return [str(value)]
        except Exception as ex:
            return [str(ex)]

        return ["ok"]
