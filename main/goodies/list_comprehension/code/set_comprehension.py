# Input list
S = ['a', 'as', 'bat', 'car', 'rac', 'dove', 'python']

# List comprehension (square brackets)
UPPERS = [len(x) for x in S]
print(UPPERS)

# Set comprehension (curly braches)
UNIQUE_LENGTHS = {len(x) for x in S}
print(UNIQUE_LENGTHS)

"""
    [1, 2, 3, 3, 3, 4, 6]
    {1, 2, 3, 4, 6}
"""