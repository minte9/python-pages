""" Linear Regression (one parameter)
h(x) = ax + b
Residuals, difference between the actual data points ...
and the predicted (by our model) values
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

# Draw 
fig, ax = plt.subplots()
ax.plot(x, y, 'x', color='g', label='training data')
plt.ylim(0, 140)
plt.xlim(0, 140)
plt.legend() #, plt.show()

# Learning a prediction function
r = LinearRegression().fit(x, y)
a = r.coef_[0][0].round(1)
b = r.intercept_[0].round(1)
print(f'Coeficient (parameter a): {a}') # 1.3
print(f'Intercept (parameter b): {b}') # -18

# Draw
ax.plot(x, a*x + b, label=f'h(x) = {b} + {a}x')
plt.legend() #, plt.show()

# Predicted values (for train dataset)
P = []
for i in x:
    P.append(-18 + 1.3*i)
print(f'Predicted values: {P}')  # 21, 41.8, 60, ... 

# Residuals
R = []
for i in range(len(x)):
    R.append(y[i] - P[i])
print(f'Residuals: {R}') # 10, -11.8, 20, ...

# Sum of squared residuals (SSR)
ssr = 0
for i in R:
    ssr += i**2
print(f'SSR = {ssr}') # 1248.15

# Draw
for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c')

# Predict unknown
x = 80
y = -18 + 1.3*x
print(f'Prediction x={x} -> {y}')
ax.plot(x, y, 'o', color='r', label=f'h({x}) = {y}')

plt.legend()
plt.show()