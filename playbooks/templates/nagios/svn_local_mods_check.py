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

p = subprocess.Popen("svn stat {{ monitored_svn_path }}",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     shell=True)

mod_apps = []
app_name = 'top level'

for line in iter(p.stdout.readline, b''):
    line = line.strip()

    if not len(line):
        continue

    if re.match(r"^X ", line):
        continue

    m = re.search(r"^Performing status on external item at "
                  r"'{{ monitored_svn_path }}/([\w-]+)'",
                  line)
    if m:
        app_name = m.group(1)
        continue

    if app_name not in mod_apps:
        mod_apps.append(app_name)

if len(mod_apps):
    current_exit_code = 1
    print("Modifications for {{ monitored_svn_path }} in %s " % (
        ', '.join(mod_apps)))

sys.exit(current_exit_code)
