"""Display all installed python modules
From command line use: pip list
"""
import pkg_resources

pkgs = pkg_resources.working_set
pkgs = sorted([
    '%s \t %s' % (k.version, k.project_name)
    for k in pkgs
])

print('\n'.join(pkgs))