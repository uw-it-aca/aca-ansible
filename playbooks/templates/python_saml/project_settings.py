INSTALLED_APPS += {% if django_version is version_compare('2', '>=') %}[{% else %}({% endif %}
'uw_saml',{% if django_version is version_compare('2', '>=') %}]{% else %}){% endif %}

ALLOWED_HOSTS += {% if django_version is version_compare('2', '>=') %}[{% else %}({% endif %}
'{{ sp_hostname }}',{% if django_version is version_compare('2', '>=') %}]{% else %}){% endif %}

SAML_USER_ATTRIBUTE = '{{ saml_user_attribute|default("uwnetid") }}'
SAML_FORCE_AUTHN = {{ sp_force_authn|default(False) }}

{% if django_version is version_compare('2', '>=')  %}
from django.urls import reverse_lazy
{% else %}
from django.core.urlresolvers import reverse_lazy
{% endif %}

LOGIN_URL = reverse_lazy('saml_login')
LOGOUT_URL = reverse_lazy('saml_logout')

UW_SAML = {
    'strict': True,
    'debug': True,
    'sp': {
        'entityId': '{{ sp_entity_id }}',
        'assertionConsumerService': {
            'url': 'https://{{ sp_hostname }}/saml/sso',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
        },
        'singleLogoutService': {
            'url': 'https://{{ sp_hostname }}/saml/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'NameIDFormat': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
        'x509cert': '''{{ sp_x509_cert }}''',
        {% if sp_private_key|default(None) %}'privateKey': '{{ sp_private_key }}',{% endif %}
    },
    'idp': {
        'entityId': '{{ idp_entity_id }}',
        'singleSignOnService': {
            'url': '{{ idp_sso_url }}',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'singleLogoutService': {
            'url': '{{ idp_logout_url }}',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'x509cert': '''{{ idp_x509_cert }}''',
    },
    'security': {
        'authnRequestsSigned': {{ sp_authn_requests_signed|default(False) }},
        'wantMessagesSigned': {{ sp_want_messages_signed|default(True) }},
        'wantAssertionsSigned': {{ sp_want_assertions_signed|default(False) }},
        'wantAssertionsEncrypted': {{ sp_want_assertions_encrypted|default(False) }},
        {% if sp_use_2fa|default(False) %}'requestedAuthnContext': ['urn:oasis:names:tc:SAML:2.0:ac:classes:TimeSyncToken'],
        'failOnAuthnContextMismatch': True,{% endif %}
    }
}
