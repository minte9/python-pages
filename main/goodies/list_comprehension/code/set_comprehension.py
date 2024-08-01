# Input list
S = ['a', 'as', 'bat', 'car', 'rac', 'dove', 'python']

# List comprehension (square brackets)
L = [len(x) for x in S]
print(L)

# Set comprehension (curly braches, unique items)
U = {len(x) for x in S}
print(U)

"""
    [1, 2, 3, 3, 3, 4, 6]
    {1, 2, 3, 4, 6}
"""