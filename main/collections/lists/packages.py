"""Display all installed python modules
CLI commands examples: 
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
    # usb-creator 0.3.7
    # wadllib 1.3.3
    # wheel 0.34.2
    # xkit 0.0.0