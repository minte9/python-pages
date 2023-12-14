import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

B = A + 100

print("Broadcasted: \n", B)

"""
    Broadcasted: 
    [[101 102 103]
     [104 105 106]
     [107 108 109]]
"""
