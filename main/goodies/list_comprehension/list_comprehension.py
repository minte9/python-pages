# Without list comprehension
# Normal use of a for loop ...

str = "abc"
C1 = []

for s in str:
    C1.append(s.capitalize())

print(C1) # ['A', 'B', 'C']


# With list comprehension
# More concise but are harder to debug ...

str = "abc"
C2 = [s.capitalize() for s in str]

print(C2) # ['A', 'B', 'C']


assert C1 == C2