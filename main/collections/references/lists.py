# References are different with lists ...
# because lists are mutable

A = [1, 2, 3]
B = A

A[1] = 'x'

assert A == [1, 'x', 3] # pass
assert B == [1, 'x', 3] # pass

# Even the code touches only A list ...
# both A and B have changed!
#
# Values stored in A and B both refer to the same list