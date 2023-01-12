""" Linear Regression (two parameters)
h(x) = ax + by + c
We can predict the CO2 emission of a car based on the size of the engine, 
but with multiple regression we can throw in more variables, 
like the weight of the car, to make the prediction more accurate
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import pathlib
import warnings  # fitted without feature names
warnings.filterwarnings("ignore", category=Warning)

DIR = pathlib.Path(__file__).resolve().parent
with open(DIR / 'data/cars.csv') as file:
    df = pd.read_csv(DIR / 'data/cars.csv')
    X = df[[
        'Weight',
        'Volume',
    ]].values
    y = df['CO2'].values

r = LinearRegression().fit(X, y) 

# Visualization (surface)
Ax, Ay = np.meshgrid(
    np.linspace(df.Weight.min(), df.Weight.max(), 100),
    np.linspace(df.Volume.min(), df.Volume.max(), 100)
)
onlyX = pd.DataFrame({'Weight': Ax.ravel(), 'Volume': Ay.ravel()})
fittedY = r.predict(onlyX)
fittedY = np.array(fittedY)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Weight'], df['Volume'], df['CO2'], c='g', marker='x', alpha=0.5)
ax.plot_surface(Ax, Ay, fittedY.reshape(Ax.shape), color='b', alpha=0.3)
ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')

# Predict known
X = [1600, 1252] # Honda Civic, 1600, 1252 / 94
y = r.predict([X])
print(f'CO2: {y.round(1)}') # CO2: 101.5
ax.plot(X[0], X[1], y[0], 'o', color='r')

X = [1100, 980] # Hyundai I20, 1100, 980 / 99
y = r.predict([X])
print(f'CO2: {y.round(1)}') # CO2: 95.6
ax.plot(X[0], X[1], y[0], 'o', color='r')

# Predict unknown
X = [1200, 780] # ?
y = r.predict([X])
print(f'CO2: {y.round(1)}') # CO2: 94.8
ax.plot(X[0], X[1], y[0], 'x', color='r')

plt.show()