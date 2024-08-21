""" An assignment creates a variable and gives it value
"""

n = 17
n = n + 24


# You can assign multiple variables in one line
a, b, c = 1, 2, 3

# Output variables
print(n) 
print(a, b, c)


""" A variable must be assigned before use
"""

y = 0
y = y + 1
assert y == 1 # pass

# Variable not assigned before use
try:
    z = z + 1
except NameError:
    print('Variable z not defined')



""" In Python it is legal to reassign a variable
    An assignment can make two variables equal, but not permanent
"""

x = 5
x = 7

assert x == 7 # pass
assert x != 5 # pass

a = 1
b = 1

assert a == b # pass

a = 2

assert a != b # pass


"""
    41
    1 2 3
    Variable z not defined
"""