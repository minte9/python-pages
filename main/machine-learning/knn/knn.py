"""KNN
Supervised machine learning (ML) algorithm ...
that can be used for classification or regression tasks 
pip install -U scikit-learn
"""

from sklearn.neighbors import KNeighborsClassifier

X = [[0,0], [1,1], [2,2], [3,3]]            # training set of data points
y = [0, 1, 0, 1]                            # labels

knn = KNeighborsClassifier(n_neighbors=3)   # KNN classifier with K=3
knn.fit(X, y)                               # Fit the classifier
                   
prediction = knn.predict([[1,2]])   # predict the label of a new data point
print(prediction)                   # [0]