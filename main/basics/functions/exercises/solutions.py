""" 1. Define a function that return x%2
"""

def f(x):
    return x%2

print(f(5))
    # 1



""" 2. Import math module and display the value of sin(pi/2)
"""

import math

print(math.sin(math.pi/2))
    # 1



""" 3. Display the result of x*2 using both normal function and lambda function.
"""

def h(x):
    return x*2

h_lambda = lambda x: x*2

print(h(2))         # 4
print(h_lambda(2))  # 4