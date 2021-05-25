import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib.pyplot as plt
import joblib

DATA_FILE = 'cpdata-Copy1.csv'
data = pd.read_csv(DATA_FILE)


data['label'] = data['label'].map({'Ground Nut': 1, 'Chickpea': 2, 'Peas': 3, 'watermelon': 4, 'apple': 5, 'banana': 6, 'papaya': 7, 'millet': 8, 'Lentil': 9, 'Adzuki Beans': 10, 'rice': 11, 'maize': 12, 'wheat': 13, 'Mung Bean': 14, 'Moth Beans': 15, 'Black gram': 16, 'Jute': 17, 'Sugarcane': 18, 'orange': 19, 'Rubber': 20, 'Kidney Beans': 21, 'pomegranate': 22, 'grapes': 23, 'Tobacco': 24, 'Pigeon Peas': 25, 'Tea': 26, 'Coffee': 27, 'Cotton': 28, 'muskmelon': 29, 'mango': 30, 'Coconut': 31})

X = data.drop(columns=['label']) 
y = data['label']


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)

classifier = GaussianNB()
classifier.fit(X_train,y_train)

predictions = classifier.predict(X_test)

score = accuracy_score(y_test,predictions)

joblib.dump(classifier,'crop-predictor.joblib')


