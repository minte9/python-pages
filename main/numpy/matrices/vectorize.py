import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

B = np.vectorize(lambda x: x + 100)(A)
print(B)

"""
    Vectorized: 
     [[101 102 103]
      [104 105 106]
      [107 108 109]]
"""
