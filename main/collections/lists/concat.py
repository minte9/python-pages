# To concatenate two list use + operator

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

assert c == [1, 2, 3, 4, 5, 6]
assert c != [1, 2, 7, 5, 6]
assert c != [1, 2, 3]