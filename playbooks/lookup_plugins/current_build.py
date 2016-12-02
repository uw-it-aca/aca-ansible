import sqlite3
import datetime
import os
import platform
import re
from ansible.plugins.lookup import LookupBase

"""
This lookup plugin tracks the current build number for projects.

The value includes the output of hostname -s, so multiple hosts can
run deployments without needing to synchonize.

To use:

  vars:
    current_build_value: "{{ lookup('current_build', project_name) }}"


  tasks:
    - copy: src="something" dest="somewhere/{{current_build_value}}/file"
"""

class LookupModule(LookupBase):

    def run(self, values, **kwargs):
        build_name = values[0]
        action = values[1]

        conn = sqlite3.connect('builds.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS builds (current_build INTEGER, name TEXT UNIQUE)")
        conn.commit()

        if "SET" == action:
            c.execute('SELECT current_build FROM builds WHERE name = ?', (build_name, ))
            row = c.fetchone()
            if row is None:
                value = 1
            else:
                value = row[0] + 1
            c.execute("REPLACE INTO builds (name, current_build) VALUES (?, ?)", (build_name, value, ))
            conn.commit()
        else:
            c.execute('SELECT current_build FROM builds WHERE name = ?', (build_name, ))
            row = c.fetchone()
            value = row[0]

        c.close()
        hostname = platform.node()
        username = os.environ['USER']
        date = datetime.date.today().isoformat()
        shortname = re.match('^([^.]+)', hostname).groups()[0]

        value = "{0}-{1}-{2}-{3}".format(hostname, username, date, value)

        return [value]
