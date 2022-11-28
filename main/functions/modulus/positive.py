"""Modulus operation 
Python always does floor division
dividend % divisor = reminder
"""

assert 0 % 7 == 0
assert 1 % 7 == 1
assert 3 % 7 == 3  # 3//7 = 0 reminder 3
assert 7 % 7 == 0
assert 8 % 7 == 1
assert 9 % 7 == 2
assert 25 % 7 == 4
assert 7 % 25 == 7 # 7//25 = 0 reminder 7

print('Tests passed')