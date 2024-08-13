""" The time module provides a function that returns the current GMT in “the epoch”
    Let's write a function that returns days, hours, minutes, seconds 
    since Unix birthday 01.01.1970
"""

import time

def time_since_epoch(t):

    d = int(t) // (3600 * 4)
    remainder = int(t) % (3600 * 4)

    h = remainder // 3600
    remainder = remainder % 3600

    m = remainder // 60
    remainder = remainder % 60

    s = remainder

    return d, h, m, s

today = time.time()
print(today)

d, h, m, s = time_since_epoch(today)

print(f"{d} days + {h} hours + {m} + minutes + {s} seconds")

"""
    1723554566.2235808
    119691 days + 1 hours + 9 + minutes + 26 seconds
"""