#!/usr/bin/python

######
#
# This script is created by ansible.  Don't edit here - update your build as needed then redeploy.
#
######

import subprocess
import sys
import os


actual = '{{ base_dir }}/tmp/crontab.actual'

if os.path.isfile(actual):
    p = subprocess.Popen(
        "diff --ignore-matching-lines='^#' %s {{ monitored_crontab_path }}" % actual,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    for line in iter(p.stdout.readline, b''):
        if len(line):
            print("Crontab differs from {{ monitored_crontab_path }}\n\n%s" % line)
            sys.exit(1)

else:
    print("Crontab not readable")
    sys.exit(1)

print("OK")
sys.exit(0)
