# Input string
str = "abcd"

# For Loop without list comprehension (less concise, but easier to debug)
res = []
for s in str:
    if s in ['a', 'b', 'c']:
        res.append(s.capitalize())

print(res) 
    # ['A', 'B', 'C']

# For Loop with list comprehension (more concise)
res2 = [s.capitalize() for s in str if s in ['a', 'b', 'c']]

print(res2)
    # ['A', 'B', 'C']

# Assertion
assert res == res2