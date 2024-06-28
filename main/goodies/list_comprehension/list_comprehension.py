# For Loop - With list comprehension 
# More concise but are harder to debug ...

str = "abcd"
D = [s.capitalize() for s in str if s in ['a', 'b', 'c']]

# For Loop - Without list comprehension 
# Normal use of a for loop ...

str = "abcd"
E = []
for s in str:
    if s in ['a', 'b', 'c']:
        E.append(s.capitalize())

# Output

print(D) # ['A', 'B', 'C']
print(E) # ['A', 'B', 'C']

assert D == E