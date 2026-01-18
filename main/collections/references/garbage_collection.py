# ---------------------------------------
# GARBAGE COLLECTION
# ---------------------------------------
# Python frees objects automatically
# when no references remain.

import sys

a = [1, 2, 3]

# Number of references to the object
print(sys.getrefcount(a))   # 2 (a + argument to getrefcount())

b = a                       # add another reference
print(sys.getrefcount(a))   # 3

del b                       # remove a reference
print(sys.getrefcount(a))  # 2

del a                       # no reference left

# Object is garbage collected automatically