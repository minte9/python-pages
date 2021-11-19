# Function distance() ...
#
# Distance between two points ...
# takes 2 Point() objects as argument
# returns the distance between them

import math

class Point: """ a 2D point """

def distance_between_points(p1, p2):
    dx = (p2.x - p1.x)**2
    dy = (p2.y - p1.y)**2
    return math.sqrt(dx + dy)

a = Point()
a.x = 0
a.y = 0

b = Point()
b.x = 3
b.y = 4

assert distance_between_points(a, b) == 5