# Python's automatic garbage collection ...
# delete any values not being referred to by any variables
#
# Manual memory management in other programming languages ...
# is a common source of bugs

import sys

a = 'm9 string'
assert sys.getrefcount(a) == 4

b = a
assert sys.getrefcount(a) == 5

c = b
assert sys.getrefcount(a) == 6

del b
assert sys.getrefcount(a) == 5

del c
assert sys.getrefcount(a) == 4