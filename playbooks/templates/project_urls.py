{% if django_version is version_compare('2', '>=') %}
from django.urls import include, re_path
{% elif django_version is version_compare('1.9', '>=') %}
from django.conf.urls import include, url
{% else %}
from django.conf.urls import patterns, include, url
{% endif %}

{% if extra_urls_head_section|default(None) %}
{% include extra_urls_head_section %}
{% endif %}

{% if django_version is version_compare('1.9', '>=') %}
urlpatterns = [
{% else %}
urlpatterns = patterns('',
{% endif %}
    {% for definition in project_url_definitions %}
    {{ definition }},
    {% endfor %}
{% if django_version is version_compare('1.9', '>=') %}
]
{% else %}
)
{% endif %}
