"""
    Conditional expression are very useful when using recursion

    Factorial number:
        0! is 1
        n! = n(n-1)!
"""

def factorial(n):
    """
        if (n == 0): 
            return 1
        else:
            return n * factorial(n-1)
    """

    return 1 if n == 0 else (n * factorial(n-1))

assert factorial(3) == 6
assert factorial(0) == 1
assert factorial(4) == 24

print("Test passed!")