"""
pip install -U scikit-learn
"""
from sklearn.neighbors import KNeighborsClassifier

# Assume we have a training set of data points with corresponding labels
X = [[0,0], [1,1], [2,2], [3,3]]  # data points
y = [0, 1, 0, 1]  # labels

# Create a KNN classifier with K=3
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier to the training data
knn.fit(X, y)

# Use the classifier to predict the label of a new data point
x_new = [1,2]  # new data point
prediction = knn.predict([x_new])  # predict the label of x_new

print("Prediction:", prediction)  # should output "Prediction: [0]"