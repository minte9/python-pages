""" LISTS - CONCATENATION
-------------------------
To concatenate two list use + operator.
To multiply a list use * operator.
----------------------------------
"""

A = [1, 2] + [3,4]  # concatenation

B = [9] * 4         # multiplication
C = [1, 2] * 2      

assert A == [1, 2, 3, 4]
assert B == [9, 9, 9, 9]
assert C == [1, 2, 1, 2]

print('Tests passed')