#!/usr/bin/python

######
#
# This script is created by ansible.  Don't edit here - update your build as needed then redeploy.
#
# If you are looking at this script because it failed to connect, you can run this mysql command:
# CREATE USER '{{ nagios_mysql_user|default('nagios') }}'@'localhost' IDENTIFIED BY '{{ mysql_password }}';
# GRANT PROCESS ON *.* TO '{{ nagios_mysql_user|default('nagios') }}'@'localhost';
#
######

import subprocess
import sys
import re
import os


slaves = [{% if "mysql-db-server-slave" in groups %}{% for host in groups["mysql-db-server-slave"] %}'{{ host }}',{% endfor %}{% endif %}]

p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'show processlist'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

content = ""
for line in iter(p.stdout.readline, b''):
    content += line

if re.match(r'.*Access denied for user', content):
    print 'Access denied.  Read %s for details' % os.path.realpath(__file__)
    sys.exit(3)

if not len(slaves):
    print 'No slave hosts defined'
    sys.exit(3)

err_slaves = []
for slave in slaves:
    if not re.search(r'repl\s+' + re.escape(slave), content):
        err_slaves.append(slave)

if len(err_slaves):
    print '%s not connected for replication' % (', '.join(err_slaves))
    sys.exit(2)

print '%s connected for replication' % (', '.join(slaves))
sys.exit(0)
