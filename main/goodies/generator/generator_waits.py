# A generator object knows how to iterate a sequence of values.
#
# Unlike list, a generator does not compute the values at once.
# It waits to be asked.
#
# A generator expression are similar with list comprehesion,
# but with parantheses instead of square brakets


g = (x**2 for x in range(3))
assert next(g) == 0
assert next(g) == 1
assert next(g) == 4

try:
    assert next(g) == 9
except StopIteration:
    print("StopIteration exception found")


# Populate a list using for loop, automatically invokes __next__
list = []
for x in range(101010): # __next__
    list.append(x)

assert len(list) != 1
assert len(list) == 101010