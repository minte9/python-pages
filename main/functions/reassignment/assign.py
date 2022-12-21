"""A variable must be assign before use
"""

y = 0
y = y + 1
assert y == 1 # pass

try:
    z = z + 1
except NameError:
    print('Variable z not defined')