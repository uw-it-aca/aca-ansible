INSTALLED_APPS.append('uw_saml')
ALLOWED_HOSTS.append('{{ sp_hostname }}')

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('saml_login')

UW_SAML = {
    'strict': True,
    'debug': True,
    'sp': {
        'entityId': '{{ sp_entity_id }}',
        'assertionConsumerService': {
            'url': 'https://{{ sp_hostname }}' + reverse_lazy('saml_sso'),
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
        },
        'singleLogoutService': {
            'url': 'https://{{ sp_hostname }}' + reverse_lazy('saml_logout'),
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'NameIDFormat': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified',
        'x509cert': '{{ sp_x509_cert }}',
        # for encrypted saml assertions uncomment and add the private key
        # 'privateKey': '',
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
        'x509cert': '{{ idp_x509_cert }}'
    },
    'security': {
        # for 2FA uncomment this line
        # 'requestedAuthnContext':  ['urn:oasis:names:tc:SAML:2.0:ac:classes:TimeSyncToken']
    }
}
