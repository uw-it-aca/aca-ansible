#!/usr/bin/env python
import os
import sys
import site

sys.path.append('{{ base_dir }}/builds/{{ current_build_value }}/')
{% for path in manage_paths|default([]) %}
sys.path.append('{{ base_dir }}/builds/{{ current_build_value }}/{{ path }}')
{% endfor %}

site.addsitedir('{{ base_dir }}/builds/{{ current_build_value }}/lib/{{ python_interpreter|default("python2.6") }}/site-packages/')
site.addsitedir('{{ base_dir }}/mysql-libs/')

os.environ["PATH"] += os.pathsep + os.pathsep.join([
    '{{ base_dir }}/node-libs/bin/',
    '{{ base_dir }}/node-libs/node_modules/less/bin/',
])

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
