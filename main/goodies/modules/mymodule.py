"""Define a module:
When you import a module, it defines new functions, but doesn't run them.
If the program is running as a script, the test code runs.
If module is imported the test code is skiped.
"""

def myprint(str):
    print('Print from my module: %s' % str)

def mysum(a, b):
    return a + b

assert mysum(1,2)  == 3
assert mysum(-1,2) == 1


"""Test code"""
if __name__ == '__main__': 
    print('Load my module ' + __name__)