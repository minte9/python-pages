# Without list comprehension
# Normal use of a for loop ...

str = "abc"
res = []

for s in str:
    res.append(s.capitalize())

print(res) 
    # ['A', 'B', 'C']


# With list comprehension
# More concise but are harder to debug ...

str = "abc"
res = [s.capitalize() for s in str]

print(res) 
    # ['A', 'B', 'C']