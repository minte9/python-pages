""" Slice operator [:] works on list, as with strings
The value -1 refers to the last index in a list
"""

a = "abcde"

assert a[:1]  == "a"
assert a[1:]  == "bcde"
assert a[1:3] == "bc" # limit 3 not included

A = [1, 2, 3, 4, 5]

assert A[:1]   != 1
assert A[:1]   == [1]
assert A[1:]   == [2, 3, 4, 5]
assert A[1:3]  == [2, 3] # limit 3 not included
assert A[-1]   == 5
assert A[-1:]  == [5] # last

print('Tests passed')