import sqlite3

"""
This lookup plugin tracks the current build number for projects.

To use:

  vars:
    current_build_value: "{{ lookup('current_build', project_name) }}"


  tasks:
    - copy: src="something" dest="somewhere/{{current_build_value}}/file"
"""

class LookupModule(object):
    run_yet = False
    run_value = None

    def __init__(self, *args, **kwargs):
        pass

    def run(self, build_name, **kwargs):
        if LookupModule.run_yet:
            return ["%s" % LookupModule.run_value]

        conn = sqlite3.connect('builds.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS builds (current_build INTEGER, name TEXT UNIQUE)")
        conn.commit()

        c.execute('SELECT current_build FROM builds WHERE name = ?', (build_name, ))
        row = c.fetchone()
        if row is None:
            value = 1
        else:
            value = row[0]


        LookupModule.run_yet = True
        LookupModule.run_value = value

        next_value = value + 1
        c.execute("REPLACE INTO builds (name, current_build) VALUES (?, ?)", (build_name, next_value, ))
        conn.commit()
        c.close()

        return ["%s" % value]
