# -*- coding: utf-8 -*-
"""iris flower classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19vKEFQMSjScCV3TGoQsdnFwZB2xBYix0
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('IRIS.csv')
df.head()

"""# New Section

# New Section
"""

#to display stats about data
df.describe()

df.info()

#to display number of samples of each class
df['species'].value_counts()

"""**processing the dataset**"""

#check for null values
df.isnull().sum()

"""**exploratory data analysis**"""

df['sepal_length'].hist()

df['sepal_width'].hist()

df['petal_length'].hist()

df['petal_width'].hist()

colors= ['red','orange','blue']
species=['Iris-virginica','Iris-versicolor','Iris-setosa']

for i in range(3):
  x=df[df['species']==species[i]]
  plt.scatter(x['sepal_length'],x['sepal_width'] ,c = colors[i], label=species[i])
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()

for i in range(3):
  x=df[df['species']==species[i]]
  plt.scatter(x['petal_length'],x['petal_width'] ,c = colors[i], label=species[i])
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.legend()

for i in range(3):
  x=df[df['species']==species[i]]
  plt.scatter(x['sepal_length'],x['petal_length'] ,c = colors[i], label=species[i])
plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.legend()

for i in range(3):
  x=df[df['species']==species[i]]
  plt.scatter(x['sepal_width'],x['petal_width'] ,c = colors[i], label=species[i])
plt.xlabel("sepal width")
plt.ylabel("petal width")
plt.legend()

"""**coorelation matrix**"""

df.corr()

corr=df.corr()
fig, ax=plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax , cmap='coolwarm')

"""label encoder"""

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()

df['species'] = le.fit_transform(df['species'])
df.head()

"""model training

"""

from sklearn.model_selection import train_test_split
x=df.drop(columns=['species'])
y=df['species']
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.30)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x_train, y_train)

print("accuracy : ", model.score(x_test, y_test)*100)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()

model.fit(x_train, y_train)

print("accuracy : ", model.score(x_test, y_test)*100)