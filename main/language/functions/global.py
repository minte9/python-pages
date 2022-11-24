""" Local, global variables
Local variable is destroyed after the function is called
To modify a global variable from within a function, use global statement
"""

def myfunc(a, b):
    c = a + b # Look Here
    return c

n = 0
def parse():
    global n # Look Here
    for i in range(10):
        n = i

print(myfunc(3,4))  # 7
parse(); print(n)   # 9

try:
    print(c)
except Exception as e:
    print(e) # name c not defined