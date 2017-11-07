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

p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'SELECT TIMEDIFF(now(), timestamp) > \"01:00:00\" AS delay FROM solstice.Status WHERE flag = \"mail_queue_running\"'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

content = ""
for line in iter(p.stdout.readline, b''):
    if 'mysql: [Warning]' not in line:
        content += line

if re.match('.*Access denied for user', content):
    print "Access denied.  Read %s for details" % os.path.realpath(__file__)
    sys.exit(3)

matches = re.match('^(0|1)\n$', content)

if not matches:
    print "Error parsing: %s" % content
    sys.exit(3)

if matches.group(1) == '1':
    print("OK")
    sys.exit(0)
else:
    print("Mailqueue running for longer than 60 mins")
    sys.exit(2)
