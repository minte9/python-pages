"""
pip install -U scikit-learn
pip install pandad
        https://github.com/5x12/themlsbook/blob/master/jupyter_book/chapter2/knn.md
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Training set of data points with corresponding labels
data = {
'height': [3.91, 7.09, 10.48, 9.21, 7.95, 7.62, 7.95, 4.69, 7.50, 7.11, 4.15, 7.29, 8.49, 7.44, 7.86, 3.93, 4.40, 5.5, 8.10, 8.69], 
'width':  [5.76, 7.69, 7.32, 7.20, 5.90, 7.51, 5.32, 6.19, 5.99, 7.02, 5.60, 8.38, 6.52, 7.89, 7.60, 6.12, 5.90, 4.5, 6.15, 5.82],
'fruit':  ['Mandarin', 'Apple', 'Lemon', 'Lemon', 'Lemon', 'Apple', 'Mandarin', 'Mandarin', 'Lemon', 'Apple', 'Mandarin', 'Apple', 'Lemon', 'Apple', 'Apple', 'Apple', 'Mandarin', 'Lemon', 'Lemon', 'Lemon']
} 

# Transform dataset into a DataFrame
df = pd.DataFrame(data)
print(df)

# Define X and y using the dataset
X = df[['height', 'width']].values
y = df.fruit.values

# KNN classifier with K=3
knn = KNeighborsClassifier(n_neighbors=3) 

# Fit the classifier to the training data
knn.fit(X, y)

# Predict the label for new data point
prediction = knn.predict([[9, 3]])
print(prediction)  
        # ['Lemon']

# Predict multiple labels
predictions = knn.predict([[9, 3], [4, 5], [2, 5], [8, 9], [5, 7]])
print(predictions) 
        # ['Lemon' 'Mandarin' 'Mandarin' 'Apple' 'Mandarin']