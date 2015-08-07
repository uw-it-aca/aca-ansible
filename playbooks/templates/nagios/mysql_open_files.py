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

p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'show status where variable_name=\"Open_files\"'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

content = ""
for line in iter(p.stdout.readline, b''):
    content += line

if re.match('.*Access denied for user', content):
    print "Access denied.  Read %s for details" % os.path.realpath(__file__)
    sys.exit(3)

matches = re.match('.*\nOpen_files\s+([\d]+)', content)

if not matches:
    print "Error parsing: %s" % content
    sys.exit(3)

count = int(matches.group(1))

print "%s open files" % count

# We have an open file limit of 1024

if count > 700:
    sys.exit(1)

if count > 900:
    sys.exit(2)

sys.exit(0)


