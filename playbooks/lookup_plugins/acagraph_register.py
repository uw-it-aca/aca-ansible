import oauth2
import json
import re

class LookupModule(object):
    def __init__(self, *args, **kwargs):
        pass

    def run(self, oauth_key, oauth_secret, acagraph_server, inventory, groups, restclients, include_pubcookie, *args, **kwargs):

        group = re.match('.*/(.*)', inventory).group(1)
        hosts = groups[group]

        consumer = oauth2.Consumer(key=oauth_key, secret=oauth_secret)
        client = oauth2.Client(consumer)

        # XXX - need to get replication master/slave relationships in here
        db_servers = groups["mysql-db-server"]
        app_servers = groups["django-app-server"]

        graph_data = {
            "name": group,
            "prereqs": [],
            "login_systems": [],
            "log_services": [],
            "hosts": []
        }

        for host in db_servers:
            graph_data["hosts"].append({
                "name": host,
                "role": "database",
            })

        for host in app_servers:
            graph_data["hosts"].append({
                "name": host,
                "role": "application",
            })

        try:
            if include_pubcookie:
                graph_data["login_systems"].append("Pubcookie")
        except Exception as ex:
            pass

        try:
            if "test" in restclients:
                for service in restclients["test"]:
                    graph_data["prereqs"].append("%s-eval" % service)

            if "production" in restclients:
                for service in restclients["production"]:
                    graph_data["prereqs"].append("%s" % service)
        except Exception as ex:
            pass

        try:
            value = client.request("%s/api/v1/service" % (acagraph_server),
                           method='POST',
                           body=json.dumps(graph_data),
                           headers={"Content-Type": "application/json"})
        except Exception as ex:
            print str(ex)

        return "OK"


