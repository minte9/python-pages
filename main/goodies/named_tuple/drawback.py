"""Named tuples drawback
Simple classes don't always stay simple
To add more methods you need to inherit the named tuple
"""

from collections import namedtuple
A = namedtuple('A', ['x', 'y'])

class B():
    def __init__(self, p):
        self.p = p
        self.x = p.x
        self.y = p.y

    def __str__(self):
        return 'B(%g, %g)' % (self.x, self.y)

a = A(1, 2)
b = B(A(1, 2))

assert a.x == 1
assert a.y == 2
assert b.x == 1
assert b.y == 2

print('Tests passed')