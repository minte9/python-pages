# Input list
STRINGS = ['a', 'as', 'bat', 'car', 'dove', 'python']

# List comprehension
UPPERS = [len(x) for x in STRINGS]
print(UPPERS)
    # [1, 2, 3, 3, 4, 6]

# Set comprehension (curly braches instead of square brackets)
UNIQUE_LENGTHS = {len(x) for x in STRINGS}
print(UNIQUE_LENGTHS)
    # {1, 2, 3, 4, 6}