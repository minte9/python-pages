""" Linear Regression (one parameter)
h(x) = ax + b
Residuals, difference between the actual data points ...
and the predicted (by our model) values
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

""" Dataset
"""
x = np.array([[30], [46], [60], [65], [77], [95]])
y = np.array([[31], [30], [80], [49], [70], [118]])

# Draw
fig, ax = plt.subplots()
ax.plot(x, y, 'x', color='g', label='training data')
plt.ylim(0, 140)
plt.xlim(0, 140)
plt.legend()
    # plt.show()


""" Learning a prediction function
"""
r = LinearRegression().fit(x, y)
print(f'Coeficient (parameter a): {r.coef_[0].round(1)}') # 1.3
print(f'Intercept (parameter b): {r.intercept_.round(1)}') # -18

# Draw
legend = f'h(x) = {r.coef_[0].round(1)}x + {r.intercept_[0].round(1)}'
ax.plot(x, r.coef_[0]*x + r.intercept_, label=legend)
plt.legend() 
    # plt.show()


""" Residuals
"""
P = [] # Predicted values (for train dataset)
for i in x:
    P.append(-18 + 1.3*i)
print(f'Predicted values: {P}')  # 21, 41.8, 60, ... 

R = [] # Residuals
for i in range(len(x)):
    R.append(y[i] - P[i])
print(f'Residuals: {R}') # 10, -11.8, 20, ...

ssr = 0 # Sum of squared residuals (SSR)
for i in R:
    ssr += i**2
print(f'SSR = {ssr}') # 1248.15

# Draw
for i in range(len(x)):
    ax.plot([x[i], x[i]], [P[i], y[i]], '-', color='c')


""" Figure
"""
plt.show()