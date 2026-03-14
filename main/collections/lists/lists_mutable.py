""" LISTS - MUTABLE
-------------------
Unlike strings, lists are mutable.
A list contains multiple values in an ordered sequence.
-------------------------------------------------------
"""

A = [1, 2]

A = [3, 4]  # mutable
A[1] = 5    # mutable

assert A == [3, 5]
assert A != [1, 2]

print('Tests passed')