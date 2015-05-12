import os
import sys
import site

sys.path.append('{{ base_dir }}/builds/{{ current_build_value }}/')
sys.path.append('{{ base_dir }}/mysql-libs/')

site.addsitedir('{{ base_dir }}/builds/{{ current_build_value }}/lib/python2.6/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
