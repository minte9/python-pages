# Class definition
#
# Use docstring to lists attributes

 
class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner
    """

class Point:
    """A 2-D point"""
    # simple comment (not used by __doc__)

print(Rectangle.__doc__) 
    # Represents a rectangle.
    #     attributes: width, height, corner - Look Here

print(Point.__doc__) 
    # A 2-D point


box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point() # corner - embeded object
box.corner.x = 10
box.corner.y = 20

assert box.width == 100
assert box.corner.x == 10