""" SET COMPREHENSION
---------------------
Set comprehension uses curly braches instead of square brackets.
Set automatically remove duplicates.
"""

A = ['a', 'as', 'bat', 'car', 'rac', 'dove', 'python']  # list

L = [len(x) for x in A]  # List comprehension
S = {len(x) for x in A}  # Set comprehension

print(L)  # [1, 2, 3, 3, 3, 4, 6]
print(S)  # {1, 2, 3, 4, 6}