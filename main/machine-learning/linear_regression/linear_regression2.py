""" Linear Regression
h(x) = ax + b
Residuals, difference between the actual data points ...
and the predicted (by our model) values
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore", category=Warning)

x = np.array([[30], [46], [60], [65], [77], [95]]) # Dataset
y = np.array([31, 30, 80, 49, 70, 118])

r = LinearRegression().fit(x, y) # Learning a prediction function
a = r.coef_[0].round(1)
b = r.intercept_.round(1)

P = [] # Predictions values (for train dataset)
for i in x:
    P.append(a*i + b)

R = [] # Residuals
for i in range(len(x)):
    R.append(y[i] - P[i])

SSR = 0 # Sum of squared residuals
for i in R:
    SSR += i**2

print(f'Predicted values: {P}')
print(f'Residuals: {R}')
print(f'SSR = {SSR}')

fig, ax = plt.subplots()

ax.plot(x, y, 'x', color='g', label='training data')
ax.plot(x, r.coef_[0]*x + r.intercept_, label=f'h(x) = {b.round(1)} + {a.round(1)}x')

for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c') # VisibleDeprecationWarning
    
plt.ylim(0, 140)
plt.xlim(0, 140)
plt.legend()
plt.show()