"""Regex: Grouping with parenthesses
"""
import re

text = 'My number is 415-555-1234'
pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
result = pattern.search(text)
code, number = result.groups()

assert code == '415'
assert number == '555-1234'
assert number != '415-555-1234'