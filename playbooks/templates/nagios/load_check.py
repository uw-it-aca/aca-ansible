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

p = subprocess.Popen("uptime", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

output = ""
for line in iter(p.stdout.readline, b''):
    output += line

matches = re.match('.*load average: (.*), (.*), (.*)', output)

load_one = float(matches.group(1))
load_five = float(matches.group(2))
load_fifteen = float(matches.group(3))

current_exit_code = 0

if load_one > {{ monitored_load.warning.one }}:
    if current_exit_code < 1:
        current_exit_code = 1

if load_five > {{ monitored_load.warning.five }}:
    if current_exit_code < 1:
        current_exit_code = 1

if load_fifteen > {{ monitored_load.warning.fifteen }}:
    if current_exit_code < 1:
        current_exit_code = 1

if load_one > {{ monitored_load.critical.one }}:
    if current_exit_code < 2:
        current_exit_code = 2

if load_five > {{ monitored_load.critical.five }}:
    if current_exit_code < 2:
        current_exit_code = 2

if load_fifteen > {{ monitored_load.critical.fifteen }}:
    if current_exit_code < 2:
        current_exit_code = 2

print "Load Averages: %s, %s, %s" % (load_one, load_five, load_fifteen)

sys.exit(current_exit_code)
