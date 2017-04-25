import oauth2
import json
import re
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, values, *args, **kwargs):
        oauth_key = values[0]
        oauth_secret = values[1]
        acagraph_server = values[2]
        inventory = values[3]
        groups = values[4]
        restclients = values[5]
        include_pubcookie = values[6]
        include_shibboleth = values[7]

        group = re.match('.*/(.*)', inventory).group(1)
        hosts = groups[group]

        consumer = oauth2.Consumer(key=oauth_key, secret=oauth_secret)
        client = oauth2.Client(consumer)

        # XXX - need to get replication master/slave relationships in here
        db_servers = groups.get("mysql-db-server", [])
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
            if include_shibboleth:
                graph_data["login_systems"].append("Shibboleth")
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


