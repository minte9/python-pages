# Tu multiply a list use * operator

a = [2]
b = [2] * 4

assert b == [2, 2, 2, 2]
assert b != 8
assert b != [ [2], [2], [2], [2] ]