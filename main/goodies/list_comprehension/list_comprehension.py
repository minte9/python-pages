# For Loop - With list comprehension 
# More concise but are harder to debug ...

str = "abc"
D = [s.capitalize() for s in str]

# For Loop - Without list comprehension 
# Normal use of a for loop ...

str = "abc"
E = []
for s in str:
    E.append(s.capitalize())

# Output

print(D) # ['A', 'B', 'C']
print(E) # ['A', 'B', 'C']

assert D == E