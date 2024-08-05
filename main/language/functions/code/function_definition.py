""" Specify the name and the sequence of statements.  
Later, you can call the function by name.  
To end the function, you have to enter an empty line.  
Split a single instruction on multple lines with \
"""

def f(a): 
    return a%2

def h(x):
    return

print(f(3))
print(h("2"))

print("Hello " + \
    "World")

"""
    1
    None
    Hello World
"""