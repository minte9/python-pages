""" Strings are immutable, you can't change them
"""

str = "Hello World"
try:
    str[0] = "J"  # invalid statement

except TypeError as e:
    print('TypeError:', e)

"""
    TypeError: 'str' object does not support item assignment
"""