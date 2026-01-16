"""List append() extend()

To add an element to a list use append()
To add a list to another list use extend()
The del statement removes values at the index in a list
"""

A = ['a', 'b', 'c']
A.append('x')

assert A != ['a', 'b', 'c']
assert A == ['a', 'b', 'c', 'x']

B = ['d', 'e']
A.extend(B)

assert A != ['a', 'b', 'c']
assert A == ['a', 'b', 'c', 'x', 'd', 'e']

del A[3]

assert A != ['a', 'b', 'c', 'x', 'd', 'e']
assert A == ['a', 'b', 'c', 'd', 'e']

print('Tests passed')