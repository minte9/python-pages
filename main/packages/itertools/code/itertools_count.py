""" Count
    Make an iterator that returns evenly spaced values beginning with start.
"""

import itertools

# without itertools
def custom_count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
counter = custom_count(10, 1)
first_five = [next(counter) for _ in range(5)]
print(first_five)

# itertools
counter = itertools.count(2.5, 0.5)
first_five = [next(counter) for _ in range(5)]
print(first_five)

"""
    [10, 11, 12, 13, 14]
    [2.5, 3.0, 3.5, 4.0, 4.5]
"""