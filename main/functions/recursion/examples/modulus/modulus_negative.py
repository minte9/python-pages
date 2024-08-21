"""Modulus with negative numbers

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