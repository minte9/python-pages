# To add an element to a list use append()
# To add a list to another list use extend()

A = ['a', 'b', 'c']
A.append('x')

assert A != ['a', 'b', 'c']
assert A == ['a', 'b', 'c', 'x']

B = ['d', 'e']
A.extend(B)

assert A != ['a', 'b', 'c']
assert A == ['a', 'b', 'c', 'x', 'd', 'e']