# ---------------------------------
# VARIABLE SWAPPING
# ---------------------------------
# Tuple unpacking makes swapping simple and save.

c = 3
d = 4

c, d = d, c

assert (c, d)   == (4, 3)


# Traditional approach (more verbose)
a = 1
b = 2

tmp = a

a = b
b = tmp

assert (a, b) == (2, 1)


# ------------------------------------------
# UNPACKING (example)
# -----------------------------------------
# Multiple variables can receive values at once.
# This is extremely common in Python code.

name, domain = "office@google.com".split('@')

assert name == "office"
assert domain == "google.com"