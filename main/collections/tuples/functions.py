# A function can return only one value, ...
# but if the value is a tuple ...
# The effect is the same as returning multiple values.

# Quontient & Reminder:
# -------------------------------------------------------------
# To compute the quontient and reminders it is better to ...
# compute both at the same time.

quot = 7//3
rem = 7%3
assert (quot, rem) == (2, 1)

quot, rem = divmod(7, 3)  # built-in function
assert (quot, rem) == (2, 1)


# Function arguments:
# -------------------------------------------------------------
# Functions can take a variable number of arguments.
# A parameter name that begins with * gathers arguments into a tuple.

t = (7, 3)
# divmod(t)  
#   TypeError: divmod expected 2 arguments, got 1

assert divmod(*t) == (2, 1)  # it works!