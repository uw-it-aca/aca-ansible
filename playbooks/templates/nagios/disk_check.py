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
pattern = r'.* ([0-9]+)%'

{% for partition in monitored_disk_partitions %}
p = subprocess.Popen("/bin/df {{ partition.path }}", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

for line in iter(p.stdout.readline, b''):
    matches = re.match(pattern, str(line))
    if matches:
        percent = matches.group(1)
        if percent > {{ partition.disk_use_warning }}:
            if current_exit_code < 1:
                current_exit_code = 1
        if percent > {{ partition.disk_use_critical }}:
            if current_exit_code < 2:
                current_exit_code = 2

        print("{{ partition.path }} @ %s%%" % (percent))

{% endfor %}
sys.exit(current_exit_code)
