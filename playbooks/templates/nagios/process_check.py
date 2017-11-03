#!/usr/bin/python

######
#
# This script is created by ansible.  Don't edit here - update your build as needed then redeploy.
#
######

import subprocess
import sys


process = sys.argv[1]

p = subprocess.Popen("ps --width=5000 xau | grep -v process_check",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     shell=True)

for line in iter(p.stdout.readline, b''):
    line = line.strip()

    if not len(line):
        continue

    if process in line:
        print(line)
        sys.exit(0)

print("%s not running!" % process)
sys.exit(2)
