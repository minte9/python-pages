# A generator object knows how to iterate a sequence of values.
#
# Unlike list, ...
# it does not compute the values at once, ...
# it waits to be asked.


# Generator

g = (x**2 for x in range(3))
assert next(g) == 0
assert next(g) == 1
assert next(g) == 4
next(g) # StopIteration - Exception


# Populate a list using generator
# only once at a time

list = []
g = (x**2 for x in range(101010))
list.append(next(g))
list.append(next(g))
assert len(list) == 2
assert len(list) != 101010


# Populate a list using for loop
# it is invoking __next__ generator

list = []
for x in range(101010): # __next__
    list.append(x)

assert len(list) != 1
assert len(list) == 101010