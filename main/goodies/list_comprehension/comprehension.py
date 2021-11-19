# List comprehension
#
# The loop variable appears in expression before we get to definition
# List comprehensions are more concise but are harder to debug

str = "abc"
res = [s.capitalize() for s in str]

assert res == ['A', 'B', 'C']