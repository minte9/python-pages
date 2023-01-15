""" Gradient descent (two params, a and b)
Algorithm starts with a random value of the parameter a
Then, it finds the direction in which the function
descrease faster and takes a step in that direction, then repeat
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

def J(a, b, x, y, m): # Cost function
    J = sum((y[i] - (a*x[i]**2 + b)) for i in range(m))
    return J

def dJa(a, b, x, y, m): # Derivatives - b held fixed
    da = sum(-2 * x[i] * (y[i] - (a*x[i] + b)) for i in range(m)) 
    return da

def dJb(a, b, x, y, m): # Derivatives - a held fixed
    db = sum(-2 * 1/m * (y[i] - (a*x[i] + b)) for i in range(m))
    return db

def gradient_descent(a, b, lr=0.00001, loops=15):
    for i in range(loops):
        da = dJa(a, b, x, y, len(x))
        a = a - lr * da
    for i in range(loops):
        db = dJb(a, b, x, y, len(x))
        b = b - lr * db
    print(round(a.item(), 1), round(b.item(), 1))

gradient_descent(0, -18)    # 1.3 -18.0
gradient_descent(2.2, -18)  # 1.3 -18.0
gradient_descent(1.3, -10)  # 1.2 -10.0
gradient_descent(1.3, -12)  # 1.2 -12.0