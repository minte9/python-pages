""" Linear Regression (multiple parameters)
We can predict the CO2 emission of a car based on the size of the engine, 
but with multiple regression we can throw in more variables, 
like the weight of the car, to make the prediction more accurate
"""

from os import X_OK
import numpy as np, sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import pathlib

DIR = pathlib.Path(__file__).resolve().parent
with open(DIR / 'data/real_estate.csv') as file:
    df = pd.read_csv(file)
    X = df[[
        'X1 transaction date',
        'X2 house age',
        'X3 distance to the nearest MRT station',
        'X4 number of convenience stores',
        'X5 latitude',
        'X6 longitude',
    ]].values
    y = df['Y house price of unit area'].values
    r = LinearRegression().fit(X, y)

# Predict some train data
A = [2013.17, 13, 732.85, 0, 24.98, 121.53]     # price: 39
B = [2013.58, 16.6, 323.69, 6, 24.98, 121.54]   # price: 51
a = r.predict([A]).round(1)
b = r.predict([B]).round(1)
print(a) # 38.8
print(b) # 48.5

# Predict unknown
X = [2013.17, 33, 732.85, 0, 24.98, 121.53]     # A with house_age = 33
y = r.predict([X]).round(1)
print(y) # 33.4