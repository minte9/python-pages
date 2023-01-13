""" Parameterized SSR (cost function) (p64)
f(x) = ax + b
How can we build an algorithm to find the best fit parameter for f(x)
First, we need a way to measire the goodness-of-fit (SSR)
Second, search over all posible values of a and b (gradient descent)
"""

import matplotlib.pyplot as plt
import numpy as np

# Training Dataset
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

fig, ax = plt.subplots()
plt.ylim(0, 140)
plt.xlim(0, 140)
ax.plot(x, y, 'o', color='g', label='training data') # training points

# Generate some a range values
A = np.linspace(-2, 4.5, 13)
for a in A:
    print(a.round(), end=', ')
    """
        -2.0, -1.0, -1.0, -0.0, 0.0, 
        1.0, 1.0, 2.0, 2.0, 3.0, 
        3.0, 4.0, 4.0
    """

# Plot regression lines (for each a)
for i in range(len(A)):
    ax.plot(x, -18 + A[i]*x, label=f'f(x) = -18 + {A[i].round(1)}x') # lines
plt.xlabel("x")
plt.ylabel("f(x)")  
plt.legend() #; plt.show()

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
    print(f'a = {a.round(1)} SSR = {np.sum(SR).round()}')
    """
        a = -2.0 SSR = 282654.0
        a = -1.5 SSR = 197923.0
        a = -0.9 SSR = 128329.0
        a = -0.4 SSR = 73872.0
        a = 0.2  SSR = 34552.0
        a = 0.7  SSR = 10368.0
        a = 1.2  SSR = 1320.0
        a = 1.8  SSR = 7409.0
        a = 2.3  SSR = 28635.0
        a = 2.9  SSR = 64998.0
        a = 3.4  SSR = 116497.0
        a = 4.0  SSR = 183133.0
    """

# Define cost function J (SSR(a))
def J(a, b, x, y, m):
    J = 0
    for i in range(m):
        J += (y[i] - (a*x[i] + b))**2
    return J

# Plot Cost function for coeficient a
fig, ax = plt.subplots()
ax.plot(A, J(A, -18, x, y, m=len(x))) # points
for a in A:
   ax.plot(a, J(a, -18, x, y, m=len(x)), 'o', label='J(%.1f, -18)' %a) # line
plt.legend() #; plt.show()

# Plot for two parameters
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
a0 = np.linspace(-1,4,20)
a1 = np.linspace(-100,100,10)
aa0, aa1 = np.meshgrid(a0, a1)
ax.plot_surface(aa0, aa1, J(aa0,aa1,x,y,m=len(x)))
ax.view_init(50,-150)
plt.show()