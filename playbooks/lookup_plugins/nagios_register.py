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

        except Exception as ex:
            return [str(ex)]

        return ["ok"]
