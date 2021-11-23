# Modulus with negative numbers:
# 
# Python modulus (%) always return a number with ...
# the same sign as the denominator. 
#
# Python applies the distribute law of Modulo operator:
#
#   (a + b) mod n = ((a mod n) + (b mod n)) mod n
#
# Python always does floor division.


# 23 % 5 = ?
#
assert 23 // 5  ==  4
assert 23 == 4*5 + 3  # reminder 3
assert 23 % 5 ==  3


# 23 % -5 
#
assert 23 // -5 == -5
assert 23 == -5 * -5 - 2  # reminder -2
assert 23 % -5 == -2 


# -3 % 7 
#
assert -3 // 7 == -1
assert -3 == -1*7 + 4  # remainder 4
assert -3 % 7 == 4


# distributive law
#
assert (2 + 2) % 3 == 1
assert (2 + 2) % 3 == (2 % 3 + 2 % 3) % 3
assert (2 + 2) % 3 != 2 % 3 + 2 % 3