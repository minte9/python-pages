""" A local variable is destroyed after the function is called.
To modify a global variable from within a function, use global statement.
"""

def f(a, b):
    c = a + b
    return c

n = 0
def h():
    global n 
        # Look Here

    for i in range(10):
        n = i
    return n

print(f(3,4))
print(h())

try:
    print(c)
except Exception as e:
    print(e)

"""
    7
    9
    name 'c' is not defined
"""