""" Gradient descent (two params, a and b)
Algorithm starts with a random value of the parameter a, b
Then, it finds the direction in which the function
descrease faster and takes a step in that direction, then repeat
"""

import numpy as np

# Training dataset
X = np.array([30, 46, 60, 65, 77, 95])
Y = np.array([31, 30, 80, 49, 70, 118])

# The model (linear)
def predict(X, a, b):
    return X * a + b # f(x) = ax + b

# Cost function
def J(a, b):
    J = np.sum(Y - predict(X, a, b)**2)
    return J

 # Derivatives
def dJ(a, b):
    da = -2 * np.sum(X * (X - (a * X + b))) # b fixed
    db = -2 * np.sum(1 * (X - (a * X + b))) # a fixed
    return da, db

# Gradient descent
def gradient_descent(a, b, lr=0.00001, loops=15):
    for i in range(loops):
        da, db = dJ(a, b)
        a = a - lr * da
        b = b - lr * db 
    print('a =', round(a, 1), ' b =', round(b, 1))
    return a, b


# Learning
a, b = gradient_descent(0, -10)

# Prediction
print(95, round(predict(95, a, b)))
print(30, round(predict(30, a, b)))
print(77, round(predict(77, a, b)))
# 95 95
# 30 30
# 77 77