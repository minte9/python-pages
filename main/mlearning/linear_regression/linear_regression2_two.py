""" Linear Regression (two parameters)
We can predict the CO2 emission of a car based on the size of the engine, 
but with multiple regression we can throw in more variables, 
like the weight of the car, to make the prediction more accurate
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import pathlib

DIR = pathlib.Path(__file__).resolve().parent
with open(DIR / 'data/cars.csv') as file:
    df = pd.read_csv(DIR / 'data/cars.csv')
    X = df[['Weight', 'Volume']].values
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

# Predict unknown
X = [1100, 980] # CO2: 99
y = r.predict([X])
ax.plot(X[0], X[1], y[0], 'o', color='r')
print(y) # 95.64991367

plt.show()