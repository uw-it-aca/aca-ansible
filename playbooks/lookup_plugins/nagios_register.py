import oauth2
import json
import re

class LookupModule(object):
    def __init__(self, *args, **kwargs):
        pass

    def run(self, oauth_key, oauth_secret, nagios_server, inventory, groups, *args, **kwargs):
        group = re.match('.*/(.*)', inventory).group(1)
        hosts = groups[group]

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


            # Create each hosts
            for host in hosts:
                value = client.request("%s/api/v1/host" % (nagios_server),
                               method='POST',
                               body=json.dumps({"name": host, "address": host}),
                               headers={"Content-Type": "application/json"})

                # Add the hosts to the hostgroup
                value = client.request("%s/api/v1/hostgroup" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"group": group, "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the disk check check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "Disk Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})

                # Add the disk check check to this host
                client.request("%s/api/v1/service" % (nagios_server),
                               method='PATCH',
                               body=json.dumps({"service": "Inode Check",
                                                "host": host}),
                               headers={"Content-Type": "application/json"})



            # Deploy the updated nagios configuration
            value = client.request("%s/api/v1/deploy" % (nagios_server), method="POST")
            return [str(value)]
        except Exception as ex:
            return [str(ex)]

        return ["ok"]
