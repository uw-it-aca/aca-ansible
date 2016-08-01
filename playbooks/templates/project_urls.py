{% if django19|default(false) %}
from django.conf.urls import include, url
{% else %}
from django.conf.urls import patterns, include, url
{% endif %}

{% if extra_urls_head_section|default(None) %}
{% include extra_urls_head_section %}
{% endif %}

{% if django19|default(false) %}
urlpatterns = [
{% else %}
urlpatterns = patterns('',
{% endif %}
    {% for definition in project_url_definitions %}
    {{ definition }},
    {% endfor %}
{% if django19|default(false) %}
]
{% else %}
)
{% endif %}
