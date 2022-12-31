"""KNN supervised machine learning (ML) algorithm
Used for classification or regression tasks 
"""
from sklearn.neighbors import KNeighborsClassifier

# Training set of data points and Labels
X = [[0,0], [1,1], [2,2], [3,3]]    
y = [0, 1, 0, 1]

# Createa a KNN classifier with K=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predict the label of a new data point                
prediction = knn.predict([[1,2]])   
print(prediction) # [0]