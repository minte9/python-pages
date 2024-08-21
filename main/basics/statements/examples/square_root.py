""" Square roots (Newton method)

    Loops are often used to compute numerical result by starting with an ...
    aproximation and iteratively improving it

    Suppose that you want to know the square root of a
    If you start with almost any estimate x ...
    you can compute a better estimation with the following formula:
        y = (x + a/x) / 2

    For example with a = 4, x = 3
    the result is preatty close to correct answer 2
    (3 + 4/3) / 2 = 2.16666666667
"""

# Aproximation algorithm (x is the initial estimate)
def square_root(a, x):

    # First result (2.16666666667) is preatty close to correct answer (2)
    while True:
        y = (x + a/x) / 2

        if (y == x): 
            break
        
        # If we repeat the process with the new estimate it gets even closer
        x = y
        
        print(y)
    return y

y = square_root(4, 3)


# Check
import math
assert y == math.sqrt(4)

"""
    2.1666666666666665
    2.0064102564102564
    2.0000102400262145
    2.0000000000262146
    2.0
"""