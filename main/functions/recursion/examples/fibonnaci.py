""" Fibonacci sequence
    Each number is the sum of the two preceding ones.

    fb(0) = 0
    fb(1) = 1
    fb(n) = fb(n-1) + fb(n-2)
"""

def fibonacci(n):
    if (n==0): 
        return 0
        
    if (n==1): 
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5