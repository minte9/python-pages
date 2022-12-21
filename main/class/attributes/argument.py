# Function arguments ...
#
# Class instances can be pass as arguments to functions

class Point:
    """ a 2D point """

p = Point()
p.x = 1
p.y = 2

def print_point(point):
    print('(%s, %s)' % (point.x, point.y))

print_point(p) # (1, 2)