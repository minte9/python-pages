# Input string
str = "abcd"

# For Loop without list comprehension (less concise, but easier to debug)
RESULT = []
for s in str:
    if s in ['a', 'b', 'c']:
        RESULT.append(s.capitalize())
print(RESULT) 
    # ['A', 'B', 'C']

# For Loop with list comprehension (more concise)
RESULT2 = [s.capitalize() for s in str if s in ['a', 'b', 'c']]
print(RESULT2)
    # ['A', 'B', 'C']

# Assertion
assert RESULT == RESULT2