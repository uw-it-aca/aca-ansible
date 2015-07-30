#!/usr/bin/python

######
#
# This script is created by ansible.  Don't edit here - update your build as needed then redeploy.
#
######

import subprocess
import sys
import re

current_exit_code = 0

p = subprocess.Popen("mpstat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

output = ""
for line in iter(p.stdout.readline, b''):
    if re.match('.*CPU', line):
        continue
    output = line

matches = re.match('.*?([0-9\.]+)$', output)
cpu_free = float(matches.groups(1)[0])

print "CPU Free: %s%%" % cpu_free

if cpu_free < {{ monitored_cpu_idle.critical }}:
    sys.exit(2)
if cpu_free < {{ monitored_cpu_idle.warning }}:
    sys.exit(1)

sys.exit(0)

