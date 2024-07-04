# Set comprehension uses curly braches instead of square brackets

# List comprehension
STRINGS = ['a', 'as', 'bat', 'car', 'dove', 'python']
UPPERS = [x.upper() for x in STRINGS if len(x) > 2]
print(UPPERS)
    # ['BAT', 'CAR', 'DOVE', 'PYTHON']

# Set comprehension
UNIQUE_LENGTHS = {len(x) for x in STRINGS}
print(UNIQUE_LENGTHS)
    # {1, 2, 3, 4, 6}