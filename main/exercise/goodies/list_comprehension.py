# Copilot: Enable/Disable Copilot completions

str = "abcd"
res = []

# For loop withou list comprehension
for c in str:
    if c in ['a', 'b', 'c']:
        res.append(c.capitalize())

print(res)

# For loop with list comprehension

res2 = [c.capitalize() for c in str if c in ['a', 'b']]
print(res2)