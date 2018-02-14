import os
import sys
import site

sys.path.append('{{ base_dir }}/builds/{{ current_build_value }}/')
sys.path.append('{{ base_dir }}/{{ db_connector|default('mysql-libs')}}/')

site.addsitedir('{{ base_dir }}/builds/{{ current_build_value }}/lib/{{ python_interpreter|default("python2.6") }}/site-packages/')
site.addsitedir('{{ base_dir }}/builds/{{ current_build_value }}/lib/python2.6/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
