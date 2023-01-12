""" Linear Regression (evaluation)
Residuals, difference between the actual data points ...
and the predicted (by our model) values
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
print(f'f(x) = {a}x + {b}') # f(x) = 1.3x - 18

# Evaluate the model
P = []   # predictions (on training dataset)
R = []   # residuals  
SSR = 0  # sum of squared residuals
for i in range(len(x)):
    P.append(-18 + 1.3*x[i])
    R.append(y[i] - P[i])
    SSR += R[i] ** 2
    print(f'x = {x[i]} => y {P[i]} r = {R[i]}')

print(f'SSR: {SSR}') # 1248.15

# Draw graphics
fig, ax = plt.subplots()
plt.ylim(0, 140)
plt.xlim(0, 140)

ax.plot(x, y, 'x', color='g', label='training data')     # dataset points
ax.plot(x, a*x + b, label=f'h(x) = {b} + {a}x')          # function line
for i in range(len(x)):                                  # residuals
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c')

plt.legend(), plt.show()