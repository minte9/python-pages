""" Step 3 / Incremental Development
    Compute the sum of squares
"""

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    sum = dx**2 + dy**2
    
    return 0.0

assert distance(1, 2, 4, 6) == 0.0
assert distance(1, 2, 1, 2) == 0.0
print("Asserts passed!")