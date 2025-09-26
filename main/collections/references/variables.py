""" In Python everything is an object.
A variable is a name bound to an object in memory.
When we assign a variable to another, we'are just copying the reference.
"""

a = [1, 2, 3]
b = a  # b is now a reference to the same list object

b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]