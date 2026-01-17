""" 
    List comprehension 
"""
A = [i for i in range(3)]

# Equivalent loop
E = []
for i in range(3):
    E.append(i)

print(f"A: {A}")  # [0, 1, 2]
print(f"E: {E}")  # [0, 1, 2]


""" 
    Nested list comprehesion 
"""
M = [[i for i in range(3)] for j in range(3)]

# Equivalent loop
L = []
for j in range(3):
    L.append([i for i in range(3)])

print(f"M: {M}")  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print(f"L: {L}")  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


"""
    Permutations
"""
perms = [
    [i, j, k]
    for i in range(3)
    for j in range(3)
    for k in range(3)
    if i != j and j != k and k != i
]

print(f"P: {perms}")  
    # [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]


""" 
    Pythonic / Permutations (recommended)

    - faster
    - cleaner
    - less prone-error
"""
from itertools import permutations

perms = list(permutations([0, 1, 2]))
             
print(f"P: {perms}")
    # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
