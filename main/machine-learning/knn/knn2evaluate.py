"""KNN fruit classification, height, width / type
Evaluate the model on the training and test dataset
The score is the difference between actual and predicted labels
1.0 means the model correctly predicted all (100%)
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Training model data set
data = pd.DataFrame({
  'height': [
    3.91, 7.09, 10.48, 9.21, 7.95, 7.62, 7.95, 4.69, 7.50, 7.11, 
    4.15, 7.29, 8.49, 7.44, 7.86, 3.93, 4.40, 5.5, 8.10, 8.69
  ], 
  'width': [
     5.76, 7.69, 7.32, 7.20, 5.90, 7.51, 5.32, 6.19, 5.99, 7.02, 
     5.60, 8.38, 6.52, 7.89, 7.60, 6.12, 5.90, 4.5, 6.15, 5.82
  ],
  'fruit': [
    'Mandarin', 'Apple', 'Lemon', 'Lemon', 'Lemon', 'Apple', 'Mandarin', 
    'Mandarin', 'Lemon', 'Apple', 'Mandarin', 'Apple', 'Lemon', 'Apple', 
    'Apple', 'Apple', 'Mandarin', 'Lemon', 'Lemon', 'Lemon'
  ]
})

X = data[['height', 'width']].values
y = data.fruit.values

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Evaluate the model on the TRAINING dataset
predictions = knn.predict(X)
score = metrics.accuracy_score(y, predictions)
print(score) 
    # 0.85 (85%)

# Evaluate on TEST dataset
data = pd.DataFrame({
    'height': [4, 4.47, 6.49, 7.51, 8.34],
    'width':  [6.5, 7.13, 7, 5.01, 4.23],
    'fruit':  ['Mandarin', 'Mandarin', 'Apple', 'Lemon', 'Lemon']
})

X = data[['height', 'width']].values
y = data.fruit.values

predictions = knn.predict(X)
score = metrics.accuracy_score(y, predictions)
print(score) 
    # 1 (100%)