"""KNN is a simple, supervised machine learning (ML) algorithm
that can be used for classification or regression tasks 
"""

from sklearn.neighbors import KNeighborsClassifier

# Training set of data points
X = [[0,0], [1,1], [2,2], [3,3]]    

# Labels
y = [0, 1, 0, 1]

# KNN classifier with K=3
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier
knn.fit(X, y)

# Predict the label of a new data point                
prediction = knn.predict([[1,2]])   
print(prediction) # [0]