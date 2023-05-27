""" Avoid nested loops with itertools.product()

We can generate enerate Cartesian product of multiple lists in Python.
The Cartesian product is the set of all combinations of elements from multiple sets.
Since it is a single loop, you can simply break once for both lists.

    pip install more-tools
"""

import itertools as it

A = [1, 2, 3]
B = [10, 20, 30]

for i,j in it.product(A, B): # cartesian product

    print("i =", i, "j = ", j)
    
    if j > 10:
        break

"""
    i = 1 j =  10
    i = 1 j =  20
"""