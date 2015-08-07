import re
import hashlib

class LookupModule(object):
    """
    Generates a mysql password for the nagios user.  Designed to repeatably give
    the same password, given the same host group and nagios_mysql_user_password_seed
    variable from your group vars.
    """
    def __init__(self, *args, **kwargs):
        pass

    def run(self, inventory, groups, seed, *args, **kwargs):
        try:
            group = re.match('.*/(.*)', inventory).group(1)

            return [hashlib.sha1("%s-%s" % (group, seed)).hexdigest()]
        except Exception as ex:
            return ["EX: %s" % str(ex)]
