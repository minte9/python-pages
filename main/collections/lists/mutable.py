"""Lists are mutable
A list contains multiple values in an ordered sequence
"""

A = [1, 2]; A[1] = 3

assert A == [1, 3]
assert A != [1, 2]

print('Tests passed')