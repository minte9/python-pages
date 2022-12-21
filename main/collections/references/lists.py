""" References are different with lists
Lists are mutable
Even the code touches only A list ...
both A and B are changed!
Values stored in A and B both refer to the same list
"""

A = [1, 2, 3]; B = A; A[1] = 'x'

assert A == [1, 'x', 3]
assert B == [1, 'x', 3]

print('Test passed')