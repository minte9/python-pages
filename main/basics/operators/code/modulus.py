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



""" Modulus with negative numbers
    Python modulus always return a number with the same sign as the denominator.

In Python (%) returns same sign as the denominator
  23 = 4*5 + 3      # reminder 3
  23 = -5* 5 - 2    # reminder -2
  -3 = -1*7 + 4     # remainder 4

Python applies distribute law of Modulo
  (a + b) mod n = ((a mod n) + (b mod n)) mod n
  (2 + 2) % 3 = (2%3 + 2%3) % 3 = 1
"""

assert (2 + 2) % 3 == 1 # distribute law of Modulo
assert (2 + 2) % 3 == (2%3 + 2%3) % 3 == 1
assert (2 + 2) % 3 != 2%3 + 2%3

assert 23 % 5 ==  3     # reminder 3
assert 23 % -5 == -2    # same sign as denominator
assert -3 % 7 == 4

assert 23 // 5  ==  4   # floor division
assert 23 // -5 == -5
assert -3 // 7 == -1

print('Tests passed')