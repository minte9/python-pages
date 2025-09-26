""" Python frees memory automatically.
You don't manually do the cleaning like in other languages.
It uses reference counting for garbage collection.
"""

import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (number of references, a + argument to getrefcount())

b = a  # add another reference
print(sys.getrefcount(a))  # 3 (count increases)

del b  # remove a reference
print(sys.getrefcount(a))  # 2 (count decreases)

del a  # no reference left -> object is garbage collected automatically