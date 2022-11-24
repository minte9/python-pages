""" A function is a named sequence of statements

To end the function, you have to enter an empty line
Statements inside a function don't run until the function is called

In Python, there is value called None ...
which represents the absence of a value

Split a single instruction on multple lines with \
"""

def myfunc(a): 
    return a%2

def myprint(x):
    return

print(myfunc(3))    # 1
print(myprint("2")) # None
print("Hello " + \
        "World")    # Hello World