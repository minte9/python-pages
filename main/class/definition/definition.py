# Class definition
#
# A programmer-defined type is called a class.
# A class definition cannot be empty.

class Point:
    """ a 2D point """ # body docstring comment

class Point:
    def get():
        return (1, 1) # tuple

assert Point.get() ==  (1, 1)
assert Point.get() !=  None

p = Point()

assert Point.get() ==  (1, 1)
assert Point.get() !=  None