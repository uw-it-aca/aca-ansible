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


p = subprocess.Popen("{{ mysql_path }} -u {{ nagios_mysql_user|default('nagios') }} -p{{ mysql_password }} -e 'show slave status' -E", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

params = {}

for line in iter(p.stderr.readline, b''):
    if re.match(r'.*Access denied; you need ', line):
        print "Access denied.  Read %s for details" % os.path.realpath(__file__)
        sys.exit(3)

for line in iter(p.stdout.readline, b''):
    if re.match(r'.*Access denied for user', line):
        print "Access denied.  Read %s for details" % os.path.realpath(__file__)
        sys.exit(3)

    try:
        (key, val) = re.split(r':\s+', line, maxsplit=1)
        params[key.strip()] = val.strip()
    except:
        continue

io_running = params.get('Slave_IO_Running')
sql_running = params.get('Slave_SQL_Running')
seconds_behind = params.get('Seconds_Behind_Master')
last_error = params.get('Last_Error')

if (io_running != 'Yes' or sql_running != 'Yes'):
    print 'Replication not running: %s, seconds behind: %s' % (
        last_error, seconds_behind)
    sys.exit(2)

if last_error != '':
    print 'Replication error: %s, seconds behind: %s' % (
        last_error, seconds_behind)
    sys.exit(2)

if not re.match(r'^\d+$', seconds_behind):
    print 'Replication error: Invalid seconds behind (%s)' % seconds_behind
    sys.exit(2)

if (int(seconds_behind) != 0 and int(seconds_behind) > 2):
    print 'Replication behind by %s seconds' % seconds_behind
    sys.exit(1)

print 'Replication OK, seconds behind: %s' % seconds_behind
sys.exit(0)
