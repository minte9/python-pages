""" Factorial of a number
    0! = 1
    n! = n(n-1)! 
"""
def factorial(n):
    """
    if n == 0: # Base case
        return 1

    return n * factorial(n-1) # Recursive case
    """

    return n* factorial(n-1) if n > 0 else 1

assert factorial(3) == 6
assert factorial(0) == 1
assert factorial(4) == 24
