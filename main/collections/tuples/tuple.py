# A tuple is a comma separated values
# It is common to use parantheses, but not necessary
#
# A single value in parantheses is not a tuple
# For a single element, include the final comma
#
# Tuples are different than lists, they are immutable.

# CLASS
t = 'a', 'b', 'c'; 
t = 'a',
t = ('a', 'b', 'c')

print(type(t)) 
    # <class 'tuple'>


# NOT a tuple
# -------------------------------------------
t = ('a')
print(type(t)) 
    # <class 'str'>


# IMUTTABLE
# -------------------------------------------
mylist = [1, 2, 3]
mylist[0] = 4
print(mylist)  # [4, 2, 3]

mytuple = (1, 2, 3)
# mytuple[0] = 4
    # TypeError: 'tuple' object does not support item assignment


# REPLACE
# -------------------------------------------
# You can't modify the elements, ...
# but you can replace one tuple with another.
# ---------------------------------------------
t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[2:]
print(t)  # ('A', 'c', 'd', 'e')