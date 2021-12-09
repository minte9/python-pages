"""Time
Calculate the time of a code to run.
Code example: product of the first 100.000 numbers.
"""
import time

def product():
    p = 1
    for i in range(1, 100000):
        p = p * i
    return p

start = time.time()
prod = product()
end = time.time()

print('The result is %s digits long.' % len(str(prod)))
print('Took %s seconds to calculate.' % (end - start))
    # The result is 456569 digits long.
    # Took 3.54418683052063 seconds to calculate.