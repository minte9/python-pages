# Without list comprehension / Normal use of a for loop ...

str = "abc"
D = []

for s in str:
    D.append(s.capitalize())

# With list comprehension / More concise but are harder to debug ...

str = "abc"
E = [s.capitalize() for s in str]

# Output

print(D) # ['A', 'B', 'C']
print(E) # ['A', 'B', 'C']

assert D == E