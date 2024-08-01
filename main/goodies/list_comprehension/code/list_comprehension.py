# Input string
S = "abcd"

# Loop (easier to debug)
R = []
for s in str:
    if s in ['a', 'b', 'c']:
        R.append(s.capitalize())
print(R)

# List comprehension (concise)
R = [s.capitalize() for s in S if s in ['a', 'b', 'c']]
print(R)