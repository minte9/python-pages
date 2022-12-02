"""Variables as references
When you assign a value to a variable, you are creating that value
in computer memory, and store a reference to it
When you assign new value to a, reference to a doesn't affect b
"""

a = 42; b = a; a = 100

assert a == 100
assert b == 42

print('Tests passed')