"""KNN IT Jobs classification (skills, languages)
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


from knn5jobs_it_data import jobs
df = pd.DataFrame(jobs)
print(df)


""" Matrix of token counts
KNeighborsClassifier class expects the input data to be a numeric array or matrix
Use the CountVectorizer class from scikit-learn, which converts a collection of text documents 
(such as a list of skills and programming languages) into a matrix of token counts
"""

# Define a function to concatenate the skills and programming languages for each job
def join_features(job):
    return ' '.join(job['skills'] + job['languages'])

jobs_string = [join_features(job) for job in jobs]

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Use the fit_transform method to convert the list of strings into a matrix of token counts
X = vectorizer.fit_transform(jobs_string)

# Extract the job titles from the list of IT jobs
y = [job['title'] for job in jobs]


""" Train the model
"""

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a KNeighborsClassifier object
knn = KNeighborsClassifier(n_neighbors=1) 

# Train the model using the training set
knn.fit(X_train, y_train)


""" Accuracy
"""

predictions = knn.predict(X_test)
accuracy = knn.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')


""" Prediction
"""

# Predict the job title for an unknown set of skills and languages
unknown_job = {
    'skills': ['programming', 'web development', 'HTML', 'CSS', 'JavaScript'],
    'languages': ['Python', 'SQL', 'HTML', 'CSS', 'JavaScript']
}
unknown_job_string = join_features(unknown_job)
X_unknown = vectorizer.transform([unknown_job_string])
prediction = knn.predict(X_unknown)
print(prediction)  # ['Full Stack Developer']