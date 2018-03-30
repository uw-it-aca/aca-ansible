INSTALLED_APPS.append('uw_saml')

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
        'entityId': 'urn:mace:incommon:washington.edu',
        'singleSignOnService': {
            'url': 'https://idp.u.washington.edu/idp/profile/SAML2/Redirect/SSO',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'singleLogoutService': {
            'url': 'https://idp.u.washington.edu/idp/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
        },
        'x509cert': 'MIID/TCCAuWgAwIBAgIJAMoYJbDt9lKKMA0GCSqGSIb3DQEBBQUAMFwxCzAJBgNV\nBAYTAlVTMQswCQYDVQQIEwJXQTEhMB8GA1UEChMYVW5pdmVyc2l0eSBvZiBXYXNo\naW5ndG9uMR0wGwYDVQQDExRpZHAudS53YXNoaW5ndG9uLmVkdTAeFw0xMTA0MjYx\nOTEwMzlaFw0yMTA0MjMxOTEwMzlaMFwxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJX\nQTEhMB8GA1UEChMYVW5pdmVyc2l0eSBvZiBXYXNoaW5ndG9uMR0wGwYDVQQDExRp\nZHAudS53YXNoaW5ndG9uLmVkdTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\nggEBAMH9G8m68L0Hf9bmf4/7c+ERxgDQrbq50NfSi2YTQWc1veUIPYbZy1agSNuc\n4dwn3RtC0uOQbdNTYUAiVTcYgaYceJVB7syWf9QyGIrglZPMu98c5hWb7vqwvs6d\n3s2Sm7tBib2v6xQDDiZ4KJxpdAvsoPQlmGdgpFfmAsiYrnYFXLTHgbgCc/YhV8lu\nbTakUdI3bMYWfh9dkj+DVGUmt2gLtQUzbuH8EU44vnXgrQYSXNQkmRcyoE3rj4Rh\nhbu/p5D3P+nuOukLYFOLRaNeiiGyTu3P7gtc/dy/UjUrf+pH75UUU7Lb369dGEfZ\nwvVtITXsdyp0pBfun4CP808H9N0CAwEAAaOBwTCBvjAdBgNVHQ4EFgQUP5smx3ZY\nKODMkDglkTbduvLcGYAwgY4GA1UdIwSBhjCBg4AUP5smx3ZYKODMkDglkTbduvLc\nGYChYKReMFwxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJXQTEhMB8GA1UEChMYVW5p\ndmVyc2l0eSBvZiBXYXNoaW5ndG9uMR0wGwYDVQQDExRpZHAudS53YXNoaW5ndG9u\nLmVkdYIJAMoYJbDt9lKKMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEB\nAEo7c2CNHEI+Fvz5DhwumU+WHXqwSOK47MxXwNJVpFQ9GPR2ZGDAq6hzLJLAVWcY\n4kB3ECDkRtysAWSFHm1roOU7xsU9f0C17QokoXfLNC0d7KoivPM6ctl8aRftU5mo\nyFJkkJX3qSExXrl053uxTOQVPms4ypkYv1A/FBZWgSC8eNoYnBnv1Mhy4m8bfeEN\n7qT9rFoxh4cVjMH1Ykq7JWyFXLEB4ifzH4KHyplt5Ryv61eh6J1YPFa2RurVTyGp\nHJZeOLUIBvJu15GzcexuDDXe0kg7sHD6PbK0xzEF/QeXP/hXzMxR9kQXB/IR/b2k\n4ien+EM3eY/ueBcTZ95dgVM=',
    },
    'security': {
        # for 2FA uncomment this line
        # 'requestedAuthnContext':  ['urn:oasis:names:tc:SAML:2.0:ac:classes:TimeSyncToken']
    }
}
