"""Variables as references
When you assign 42 to a variable, you are creating 42 value
in computer memory, and store a reference to it
"""

a = 42; b = a
a = 100 # new value, store a reference to it

assert a == 100
assert b == 42 # reference to a doesn't afect b

print('Tests passed')