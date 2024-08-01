# Input list
S = ['a', 'as', 'bat', 'car', 'rac', 'dove', 'python']

# List comprehension (square brackets)
LENGTHS = [len(x) for x in S]
print(LENGTHS)

# Set comprehension (curly braches)
UNIQUE_LENGTHS = {len(x) for x in S}
print(UNIQUE_LENGTHS)