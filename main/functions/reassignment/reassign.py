# In Python it is legal to reassign a variable.
# An assignment can make two variables equal, but not permanent.

x = 5
x = 7

assert x == 7
assert x != 5

a = 1
b = 1

assert a == b

a = 2

assert a != b
