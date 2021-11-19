# Named tuples drawback ...
#
# Simple classes don't always stay simple.
# You might need to add more methods

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
assert p.x == 1
assert p.y == 2


# To add more methods ...
# you need to inherit the named tuple

class Point_new():
    def __init__(self, p):
        self.p = p
        self.x = p.x
        self.y = p.y

    def __str__(self):
        return 'Point_new(%g, %g)' % (self.x, self.y)

p = Point_new(Point(1, 2))
assert p.x == 1
assert p.y == 2