# When you assign 42 to a variable,
# you are creating 42 value in computer memory ...
# and store a reference to it
a = 42

# When you copy the value in a ....
# you are copying the reference.
b = a

# When later you change the value of a, 
# you are creating a new value and store a reference to it
a = 100

# This copy doesn't afect b
assert a == 100
assert b == 42