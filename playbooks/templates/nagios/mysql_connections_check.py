#!/usr/bin/python

######
#
# This script is created by ansible.  Don't edit here - update your build as needed then redeploy.
#
# If you are looking at this script because it failed to connect, you can run this mysql command:
# CREATE USER '{{ nagios_mysql_user|default('nagios') }}'@'localhost' IDENTIFIED BY '{{ mysql_password }}';
#
######

import subprocess
import sys
import re
import os

p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'show status where variable_name=\"Threads_connected\"'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

content = ""
for line in iter(p.stdout.readline, b''):
    if 'Warning' not in line and 'Variable_name' not in line:
        content += line

if re.match('.*Access denied for user', content):
    print "Access denied.  Read %s for details" % os.path.realpath(__file__)
    sys.exit(3)

matches = re.match('.*Threads_connected\s+([\d]+)', content)

if not matches:
    print "Error parsing: %s" % content
    sys.exit(3)

count = int(matches.group(1))

p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'show variables where Variable_name=\"max_connections\"'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

content = ""
for line in iter(p.stdout.readline, b''):
    if 'Warning' not in line and 'Variable_name' not in line:
        content += line

matches = re.match('.*max_connections\s+([\d]+)', content)

if not matches:
    print "Error parsing: %s" % content
    sys.exit(3)

max_conn = int(matches.group(1))


percent = float(count) / float(max_conn)
print "%s of %s connections used. (%s%%)" % (count, max_conn, float(int(percent * 10000))/100)

if percent > 0.7:
    sys.exit(1)
if percent > 0.9:
    sys.exit(2)

sys.exit(0)
