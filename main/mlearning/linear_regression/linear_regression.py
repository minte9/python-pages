""" Linear Regression
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
plt.xlim(0, 140) #,plt.legend(), plt.show()

# Learning a prediction function
r = LinearRegression().fit(x, y)
print(f'coeficient (parameter a): {r.coef_[0].round(1)}')
print(f'intercept (parameter b): {r.intercept_.round(1)}')

# Draw
legend = f'h(x) = {r.coef_[0].round(1)}x + {r.intercept_[0].round(1)}'
ax.plot(x, r.coef_[0]*x + r.intercept_, label=legend)

# Predicted values (for train dataset)
P = []
for i in x:
    P.append(-18 + 1.3*i)
print(f'Predicted values: {P}') #,plt.legend(), plt.show()

# Residuals
R = []
for i in range(len(x)):
    R.append(y[i] - P[i])
print(f'Residuals: {R}')

# Draw
for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c')

# Sum of squared residuals
ssr = 0
for i in R:
    ssr += i**2
print(f'SSR = {ssr}')

# Show
plt.legend()
plt.show()