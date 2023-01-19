""" Gradient descent (two params, a and b)
Algorithm starts with a random value of the parameter a, b
Then, it finds the direction in which the function
descrease faster and takes a step in that direction, then repeat
"""

import numpy as np

# The model (linear)
def predict(X, a, b):
    return X * a + b # f(x) = ax + b

# Cost function
def J(a, b):
    J = np.sum((Y - predict(X, a, b))**2)
    return J

# Derivatives
def dJ(a, b):
    da = np.sum(-2 * X * (Y - predict(X, a, b))) # b fixed
    db = np.sum(-2 * 1 * (Y - predict(X, a, b))) # a fixed
    return da, db

# Gradient descent
def gradient_descent(X, Y, lr=0.00001, loops=1000):
    a = 0
    b = 0
    for i in range(loops):
        da, db = dJ(a, b)
        a = a - lr * da
        for j in range(loops):
            b = b - lr * db
    return a, b


# Training dataset
X = np.array([30, 46, 60, 65, 77, 95])
Y = np.array([31, 30, 80, 49, 70, 118])

# Learning a,b
a, b = gradient_descent(X, Y)
print('a =', round(a, 1), ' b =', round(b,1)) # 1.3, -18
print('Predictions:', f'f(x) = {round(a, 1)}x + {round(b)}') # f(x) = 1.3x - 18

# Predictions
x = 33; y = round(predict(x, a, b)); print("fx(%s) =" %x, y)
x = 45; y = round(predict(x, a, b)); print("fx(%s) =" %x, y)
x = 62; y = round(predict(x, a, b)); print("fx(%s) =" %x, y)
    # fx(33) =  25
    # fx(45) =  41
    # fx(62) =  63