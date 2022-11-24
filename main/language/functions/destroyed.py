""" Local / global variables

Local variable is destroyed after the function is called
To modify a global variable from within a function, 
use global statement
"""

def myfunc(a, b):
    c = a + b
    return c

assert myfunc(3, 4) != None
assert myfunc(3, 4) == 7

# print(c) # NameError: name 'c' is not defined


n = 0
def parse():
    global n
    for i in range(10):
        n = i

parse()

assert n != 0
assert n == 9