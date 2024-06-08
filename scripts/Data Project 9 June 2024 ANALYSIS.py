#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

data = pd.read_csv(r"gold_price_yearly CLEANED.csv")


# In[2]:


print(data.head())
print(data.dtypes)


# In[4]:


data['HighChange'] = (data['Annual % Change'] > data['Annual % Change'].median()).astype(int)

features = ['Year Range Price', 'Year High', 'Year Low']
target = 'HighChange'

# Data cleaning to take out blanks
data_clean = data.dropna(subset=features + [target])

# Split the data into features (X) and target (y)
X = data_clean[features]
y = data_clean[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=200)

# Train a logistic regression model
clf = LogisticRegression().fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy and other metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Recall:", recall)
print("Precision:", precision)


# In[5]:


# Find correlation between features and target
correlation = data_clean.corr()

print(correlation)


# In[ ]:




