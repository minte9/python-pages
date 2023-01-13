""" Linear Regression (evaluation)
A residual is the difference between the actual data point 
and the predicted (by our model) value
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training Dataset
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

# Learn a prediction function
r = LinearRegression().fit(x, y)
a = r.coef_[0][0].round(1)
b = r.intercept_[0].round(1)

# Evaluate the model
P = [] # predictions (on training dataset)
R = [] # residuals  
SSR = 0 # sum of squared residuals

for i in range(len(x)):
    P.append(-18 + 1.3*x[i])
    R.append(y[i] - P[i])
    SSR += R[i] ** 2
    print(
        f'x = {x[i].round(1).item()} \t' +
        f'y = {P[i].round(1).item()} \t' +
        f'r = {R[i].round(1).item()}'
    )
    """
    x = 30      y = 21.0        r = 10.0
    x = 46      y = 41.8        r = -11.8
    x = 60      y = 60.0        r = 20.0
    x = 65      y = 66.5        r = -17.5
    x = 77      y = 82.1        r = -12.1
    x = 95      y = 105.5       r = 12.5
    """

print(f'f(x) = {a}x + {b}')             # f(x) = 1.3x - 18
print(f'SSR = {SSR.round(2).item()}')   # 1248.15

# Draw graphics
fig, ax = plt.subplots()
plt.ylim(0, 140)
plt.xlim(0, 140)

ax.plot(x, y, 'x', color='g', label='training data')     # dataset points
ax.plot(x, a*x + b, label=f'h(x) = {b} + {a}x')          # function line
for i in range(len(x)):                                  # residuals
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c')

plt.legend(), plt.show()