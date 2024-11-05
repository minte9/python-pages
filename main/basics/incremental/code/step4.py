""" Step 4 / Incremental Development
    Finally, use math.sqrt() to compute the result
"""

import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    sum = dx**2 + dy**2
    
    return math.sqrt(sum)

d = distance(1, 2, 4, 6)

assert distance(1, 2, 4, 6) == 5.0
assert distance(2, 2, 2, 6) == 4.0
print("Asserts passed!")