"""Regex on multiple lines
This verbose mode can be enabled with re.VERBOSE
"""
import re

pattern = re.compile(r'''
    (\d{3})  # area code
    (\s|-)?    # separator
    (
        \d{3} # 3 digits
        (\s|-)  # separator
        \d{4} # 4 digits
    )
''', re.VERBOSE)

result = pattern.search('My number is 415 555-1234')
groups = result.groups()
code, sep, number, sep = groups

assert groups == ('415', ' ', '555-1234', '-')
assert code == '415'
assert number == '555-1234'
assert number != '415-555-1234'