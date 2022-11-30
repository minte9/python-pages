"""Named tuples
When you define a class you must type a lot of code
Python provides a more concise way with named tuples
"""

class A:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

from collections import namedtuple
B = namedtuple('B', ['x', 'y'])

a = A(1, 2)
b = B(1, 2)

assert a.x == b.x == 1
assert a.y == b.y == 2

print('Tests passed')