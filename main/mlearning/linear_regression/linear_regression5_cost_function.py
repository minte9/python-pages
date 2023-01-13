""" Parameterized SSR (cost function)
f(x) = ax + b
How can we build an algorithm to find the best fit parameter for f(x)
First, we need a way to measure the goodness-of-fit (SSR)
Second, search over all posible values of a and b (gradient descent)
For start, let's pretend that b is known (-18)
"""

import matplotlib.pyplot as plt
import numpy as np

# Training Dataset
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

fig, ax = plt.subplots()
plt.ylim(0, 140)
plt.xlim(0, 140)
ax.plot(x, y, 'o', color='g', label='training data') # points

# Generate some a range values
A = np.linspace(-2, 4.5, 13) # 21 values

# Plot lines
for i in range(len(A)):
    msg ='f(x) = -18 + %sx' % A[i].round(1)
    ax.plot(x, -18 + A[i]*x, label = msg) # f(x) = -18 + -2.0x

plt.xlabel("x")
plt.ylabel("f(x)")  
plt.legend()

# Calculate SSR for each a
SSR = []
for a in A:
    P = []  # predictions
    SR = [] # square residuals
    for i in x:
        P.append(-18 + a*i)
    for i in range(0, len(x)):
        SR.append((y[i] - P[i])**2)
    SSR.append(np.sum(SR))

# Generic cost function J = SSR(a)
def J(a, b, x, y, m):
    J = 0
    for i in range(m): # number of train points
        J += (y[i] - (a*x[i] + b))**2
    return J

fig, ax = plt.subplots()
ax.plot(A, J(A, -18, x, y, m=len(x))) # J(a)
for a in A:
    msg ='J(%.1f, -18)' % a
    ax.plot(a, J(a, -18, x, y, m=len(x)), 'o', label = msg) # points
plt.xlabel("a")
plt.ylabel("SSR(a)")  
plt.legend()

# Plot for two parameters
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
a = np.linspace(-1, 4, 20)
b = np.linspace(-100, 100, 10)
aa, bb = np.meshgrid(a, b)
ax.plot_surface(aa, bb, J(aa, bb, x, y, m=len(x))) # surface
ax.view_init(50,-150)
plt.show()