import re
import hashlib
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    """
    Generates a mysql password for the nagios user.  Designed to repeatably give
    the same password, given the same host group and nagios_mysql_user_password_seed
    variable from your group vars.
    """
    def run(self, values, *args, **kwargs):
        inventory = values[0]
        groups = values[1]
        seed = values[2]

        try:
            group = re.match('.*/(.*)', inventory).group(1)

            return [hashlib.sha1("%s-%s" % (group, seed)).hexdigest()]
        except Exception as ex:
            return ["EX: %s" % str(ex)]
