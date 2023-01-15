""" Gradient descent
Algorithm starts with a random value of the parameter a
Then, it finds the direction in which the function
descrease faster and takes a step in that direction, then repeat
"""

import matplotlib.pyplot as plt
import numpy as np

# Training Dataset
X = np.array([30, 46, 60, 65, 77, 95]).reshape(6,1)
Y = np.array([31, 30, 80, 49, 70, 118])

# Cost function
def J(a, b, X, Y):
    J = 0
    for i in range(len(X)): # number of train points
        J += (Y[i] - (a*X[i] + b))**2
    return J

# Derivative of the cost function
def dJ(a, b, X, Y):
    dJ = 0
    for i in range(len(X)):
        dJ += -2*X[i]*(Y[i] - (a*X[i] + b)) # d(ax^2) = 2ax
    return dJ.item()

d = dJ(0, -18, X, Y)
print('Derivative J(a) = ', d) # -67218


# Gradient descent (algorithm)
# J(a) derivative is used to find where the SSR is the lowest

a = 0 # start value
l = 0.00001 # learning rate

a1 = a  - l * dJ(a, -18, X, Y)  # step 1
a2 = a1 - l * dJ(a1, -18, X, Y) # step 2
a3 = a2 - l * dJ(a2, -18, X, Y) # step 3

print('Step 1 a =', round(a1, 5)) # 0.67218
print('Step 2 a =', round(a2, 5)) # 0.99758
print('Step 3 a =', round(a3, 5)) # 1.15511


# Gradient descent (implementation)
def gradient_descent(a=0, b=-18, lr=0.00001, loops=15):
    for i in range(15):
        d = dJ(a, b, X, Y)
        a = a - d*lr
        # print(f'Step {i+1} a = {round(a, 5)}')
    return round(a, 5)

a = gradient_descent(0)
print(round(a, 4)) # 1.3029

a = gradient_descent(2.23) # different value for a start
print(round(a, 4)) # 1.3029


# Grapichs
fig, ax = plt.subplots()
A = np.linspace(-2, 4.5, 23) # 21 values
ax.plot(A, J(A, -18, X, Y)) # J(a)

ax.plot(a, J(a, -18, X, Y), 'o', color='g', label='a = 1.3029') # optim

ax.plot(0,  J(0,  -18, X, Y), 'o', color='r') # points
ax.plot(a1, J(a1, -18, X, Y), 'o', color='r')
ax.plot(a2, J(a2, -18, X, Y), 'o', color='r')
ax.plot(a3, J(a3, -18, X, Y), 'o', color='r')

ax.plot([0,  a1], [J(0,  -18, X, Y), J(a1, -18, X, Y)], color='r') # lines
ax.plot([a1, a2], [J(a1, -18, X, Y), J(a2, -18, X, Y)], color='r')
ax.plot([a2, a3], [J(a2, -18, X, Y), J(a3, -18, X, Y)], color='r')

plt.xlim(-2, 5)
plt.ylim(-10000, 70000)
plt.xlabel("a")
plt.ylabel("SSR(a)")  
plt.legend()
plt.show()