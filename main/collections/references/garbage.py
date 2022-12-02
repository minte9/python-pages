"""Python's automatic garbage collection
Delete any values not being referred to by any variables
Manual memory management in other programming languages ...
is a common source of bugs.
The getrefcount function returns the number of references
"""

import sys

a = 'somevalue'
assert sys.getrefcount(a) == 4
assert sys.getrefcount('somevalue') == 4

b = a; c = b
assert sys.getrefcount(a) == 6

del a; del b; del c
assert sys.getrefcount('somevalue') == 3 # Look Here

print('Tests passed')