# Modulus operation: 
# 
# dividend % divisor = reminder
#
# Python always does floor division

assert 0 % 7 == 0
assert 1 % 7 == 1
assert 2 % 7 == 2
assert 3 % 7 == 3  # 3 // 7 = 0 reminder 3
assert 7 % 7 == 0

assert 8 % 7 == 1
assert 9 % 7 == 2

assert 25 % 7 == 4
assert 7 % 25 == 7