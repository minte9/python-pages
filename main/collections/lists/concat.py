"""To concatenate two list use + operator
To multiply a list use * operator
"""

A = [1, 2] + [3,4]
B = [9] * 4
C = A * 2

assert A == [1, 2, 3, 4]
assert B == [9, 9, 9, 9]

print(C) # 1,2,3,4,1,2,3,4

print('Tests passed')