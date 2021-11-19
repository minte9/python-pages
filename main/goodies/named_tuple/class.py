# Named tuples ...
#
# When you define a class you must type a lot of code
# Python provides a more concise way with named tuples

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

p = Point(1, 2)

assert p.x == 1
assert p.y == 2


# Named tuples

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

nt = Point(3, 4)

assert nt.x == 3
assert nt.y == 4