""" Accumulate sums
    Make an iterator that returns accumulated sums  from other binary functions.
"""

import itertools

N = [1, 2, 3, 4, 5]
T = []

# without itertools
total = 0
for n in N:
    total += n
    T.append(total)
print(T)

# itertools
T = itertools.accumulate(N)
print(list(T))

"""
    [1, 3, 6, 10, 15]
    [1, 3, 6, 10, 15]
"""