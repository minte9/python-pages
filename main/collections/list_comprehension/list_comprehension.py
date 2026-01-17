""" 
    List comprehension 
"""
A = [i for i in range(3)]

# Equivalent loop
E = []
for i in range(3):
    E.append(i)

print(A)  # [0, 1, 2]
print(E)  # [0, 1, 2]


""" 
    Nested list comprehesion 
"""
M = [[i for i in range(3)] for j in range(3)]

# Equivalent loop
L = []
for j in range(3):
    L.append([i for i in range(3)])

print(M)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print(L)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


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

print(perms)  
    # [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]