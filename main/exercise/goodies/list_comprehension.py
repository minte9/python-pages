# Copilot: Enable/Disable Copilot completions

str = "abcd"
res = []

for c in str:
    if c in ['a', 'b', 'c']:
        res.append(c.capitalize())

print(res)

# List Comprehension

res2 = [c.capitalize() for c in str if c in ['a', 'b']]
print(res2)