""" Linear Regression (one parameter)
h(x) = ax + b
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

# Function
print(f'f(x) = {a}x + {b}') # f(x) = 1.3x - 18

# Predict unknown
x1 = 80
y1 = a*x1 + b
print(f'f({x1}) = {y1}') # f(80) = 86.0

# Evaluate the model
P = []
R = []
SSR = 0
for i in x:
    P.append(-18 + 1.3*i) # predictions (on training dataset)
for i in range(len(x)):
    R.append(y[i] - P[i]) # residuals
for i in R:
    SSR += i**2 # sum of squared residuals

print(f'Predictions: {P}')  # 21, 41.8, 60, ... 
print(f'Residuals: {R}')    # 10, -11.8, 20, ...
print(f'SSR: {SSR}')        # 1248.15

# Draw graphics
fig, ax = plt.subplots()
plt.ylim(0, 140)
plt.xlim(0, 140)

ax.plot(x, y, 'x', color='g', label='training data')     # dataset points
ax.plot(x, a*x + b, label=f'h(x) = {b} + {a}x')          # function line
ax.plot(x1, y1, 'o', color='r', label=f'h({x1}) = {y1}') # prediction unknown

for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c') # residuals

plt.legend(), plt.show()