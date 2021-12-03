"""Display all installed python modules
From command line use: pip list
"""
import pkg_resources

pkgs = pkg_resources.working_set
pkgs = sorted(['%s \t %s' % (k.version, k.project_name) for k in pkgs])

print('\n'.join(pkgs))
    # ...
    # 3.0.4    chardet
    # 3.1.0    oauthlib
    # 3.1.7    bcrypt
    # 3.12.0   louis
    # 3.16.0   simplejson
    # 3.36.0   PyGObject
    # ...