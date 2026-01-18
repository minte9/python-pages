# ----------------------------------------------
# TUPLES
# ----------------------------------------------
# A tuple is a comma-separated sequence of values.
# Parentheses are common, but commas define the tuple.
#
# A single value in parantheses is not a tuple.
# For a single element, include the final comma.

t1 = 'a', 'b', 'c'
t2 = ('a', 'b', 'c')

print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>


# -----------------------------
# SINGLE ELEMENT TUPLES
# -----------------------------
# Parentheses alone don NOT crete a tuple.
# The comma does.

t1 = 'a'
t2 = ('a')

print(type(t1))  # <class 'str'>
print(type(t2))  # <class 'str'>

t3 = ('a',)
print(type(t3))  # <class 'tuple'> 


# -----------------------------
# IMMUTABLE
# -----------------------------

# List are mutalbe
mylist = [1, 2, 3]
mylist[0] = 4
print(mylist)  # [4, 2, 3]

# Tuples are immutable
mytuple = (1, 2, 3)

# mytuple[0] = 4 
# TypeError: 'tuple' object does not support item assignment


# --------------------------------
# REPLACING A TUPLE
# --------------------------------
# You cannot change elements,
# but you cand bind the variable to a new tuple.

t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[2:]

print(t)   # ('A', 'c', 'd', 'e')