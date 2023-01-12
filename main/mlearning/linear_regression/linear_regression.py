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

fig, ax = plt.subplots()
ax.plot(x, y, 'x', color='g', label='training data') # draw dataset points
plt.ylim(0, 140)
plt.xlim(0, 140)
plt.legend() #, plt.show()

# Learning a prediction function
r = LinearRegression().fit(x, y)
a = r.coef_[0][0].round(1)
b = r.intercept_[0].round(1)
print(a) # 1.3
print(b) # -18

ax.plot(x, a*x + b, label=f'h(x) = {b} + {a}x') # draw function line
plt.legend() #, plt.show()

# Predict known
P = []
for i in x: # training dataset
    P.append(-18 + 1.3*i)
print(f'Predictions: {P}')  # 21, 41.8, 60, ... 

# Evaluate the model
R = [] 
for i in range(len(x)):
    R.append(y[i] - P[i])
print(f'Residuals: {R}') # 10, -11.8, 20, ...

ssr = 0
for i in R:
    ssr += i**2 # sum of squared residuals
print(f'SSR: {ssr}') # 1248.15

for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c') # draw residuals

# Predict unknown
x = 80
y = -18 + 1.3*x
print(f'x = {x} -> y = {y}') # x = 80 -> y = 86.0

ax.plot(x, y, 'o', color='r', label=f'h({x}) = {y}') # draw prediction

# Show graphics
plt.legend(), plt.show()