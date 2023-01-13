""" Gradient descent (p76)
Finding the optimal value for a.
Algorithm starts with a random value of the parameter a. 
Then, it finds the direction in which the function
descrease faster and takes a step in that direction.
Then, repeats the process.
"""

import matplotlib.pyplot as plt
import numpy as np

# Training Dataset
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

# Cost function
def J(a, b, x, y, m):
    J = 0
    for i in range(m): # number of train points
        J += (y[i] - (a*x[i] + b))**2
    return J

# Derivative of the cost function
def dJ(a, b, x, y, m):
    dJ = 0
    for i in range(m):
        dJ += -2*x[i]*(y[i] - (a*x[i] + b)) # d(ax^2) = 2ax
    return dJ.item()

d = dJ(0, -18, x, y, len(x))
print('Derivative J(a) = ', d) # -67218


# Gradient descent (algorithm)
# J(a) derivative is used to find where the SSR is the lowest

a = 0 # start value
l = 0.00001 # learning rate

a1 = a  - l * dJ(a, -18, x, y, len(x))  # step 1
a2 = a1 - l * dJ(a1, -18, x, y, len(x)) # step 2
a3 = a2 - l * dJ(a2, -18, x, y, len(x)) # step 3

print('Step 1 a =', round(a1, 5)) # 0.67218
print('Step 2 a =', round(a2, 5)) # 0.99758
print('Step 3 a =', round(a3, 5)) # 1.15511


# Gradient descent (implementation)
def gradient_descent(a=0, loops=15):
    for i in range(15):
        d = dJ(a, -18, x, y, len(x))
        a = a - d*l
        # print(f'Step {i+1} a = {round(a, 5)}')
    return round(a, 5)

a = gradient_descent(0, 15)
print(round(a, 4)) # 1.3029

a = gradient_descent(2.23, 15) # different value for a start
print(round(a, 4)) # 1.3029


# Grapichs
fig, ax = plt.subplots()
A = np.linspace(-2, 4.5, 13) # 21 values
ax.plot(A, J(A, -18, x, y, m=len(x))) # J(a)

ax.plot(0, J(0, -18, x, y, m=len(x)), 'x', color='r')       # start a
ax.plot(2.23, J(2.23, -18, x, y, m=len(x)), 'x', color='r') # start a
ax.plot(a, J(a, -18, x, y, m=len(x)), 'o', color='g')       # optim a

plt.xlabel("a")
plt.ylabel("SSR(a)")  

plt.show()