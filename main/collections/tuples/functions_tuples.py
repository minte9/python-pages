# --------------------------------------
# MULTIPLE RETURN VALUES
# --------------------------------------
# Functions return ONE object.
# That object is often a tuple.
#
# Example:
#   - Quontient & Reminder:
#
# To compute the quontient and reminders 
# it is better to compute both at the same time.

quot = 7//3
rem = 7%3

assert (quot, rem) == (2, 1)

quot, rem = divmod(7, 3)  # built-in function (returns tuple)

assert (quot, rem) == (2, 1)


# ------------------------------------------
# UNPACKING ARGUMENTS
# ------------------------------------------
# * expands a tuple into separate arguments.
#
# Functions can take a variable number of arguments.
# A parameter name that begins with * gathers arguments into a tuple.

t = (7, 3)
# divmod(t)  
# TypeError: divmod expected 2 arguments, got 1

assert divmod(*t) == (2, 1)  # it works!