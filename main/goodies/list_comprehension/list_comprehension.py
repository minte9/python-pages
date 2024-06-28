# Input string
str = "abcd"

# For Loop with list comprehension (more concise, but harder to debug)
D = [s.capitalize() for s in str if s in ['a', 'b', 'c']]

# For Loop without list comprehension (less concise, but easier to debug)
E = []
for s in str:
    if s in ['a', 'b', 'c']:
        E.append(s.capitalize())


# Output
print(D) # ['A', 'B', 'C']
print(E) # ['A', 'B', 'C']

# Assertion
assert D == E