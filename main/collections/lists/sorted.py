"""Display all installed python modules
CLI Examples: 
    pip list
    pip list --outdated
    pip show pyperclip
    pip install pyperclip
"""
import pkg_resources

pkgs = pkg_resources.working_set
pkgs = sorted(['%s \t %s' % (k.key, k.version) for k in pkgs])

print('\n'.join(pkgs))
    # ...
    # ufw 0.36
    # unattended-upgrades 0.1
    # urllib3 1.25.8