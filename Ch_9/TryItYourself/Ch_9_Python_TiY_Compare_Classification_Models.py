#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Compare Classification Models ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

# Import data
data_train = pd.read_csv('carseats_train.csv')
data_test = pd.read_csv('carseats_test.csv')

# Distinguish training and test data
x_train = data_train[['competitor_price', 'income', 'advertising', 'population', 'price', 'age', 'education']]
x_test = data_test[['competitor_price', 'income', 'advertising', 'population', 'price', 'age', 'education']]

y_train = data_train['sales_cat'].astype('category').cat.rename_categories({'Low': 0, 'High': 1})
y_test = data_test['sales_cat'].astype('category').cat.rename_categories({'Low': 0, 'High': 1})

## Logistic Regression
regression_pipeline = Pipeline(
  [('lr', LogisticRegression())]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_test)
accuracy_1 = accuracy_score(y_test, y_predicted)

## Classification Tree (Max Depth = 5)
tree_pipeline = Pipeline(
  [('tree', DecisionTreeClassifier(max_depth=5, random_state=1234))]
).set_output(transform='pandas')

tree_fitted = tree_pipeline.fit(x_train, y_train)
y_predicted = tree_pipeline.predict(x_test)
accuracy_2 = accuracy_score(y_test, y_predicted)

## Classification Random Forest (Min n = 10)
forest_pipeline = Pipeline(
  [('rf', RandomForestClassifier(min_samples_split=10, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

accuracy_3 = accuracy_score(y_test, y_predicted)


## Classification kNN (k = 5)
knn_pipeline = Pipeline(
  [('knn', KNeighborsClassifier(n_neighbors=5, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(x_train, y_train)

y_predicted = knn_pipeline.predict(x_test)

accuracy_4 = accuracy_score(y_test, y_predicted)

# Create data frame of model results
model_vs_accuracy = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest', 'kNN'],
    'Test Accuracy': [accuracy_1, accuracy_2, accuracy_3, accuracy_4]
})
model_vs_accuracy = model_vs_accuracy.round({'test_accuracy' : 2})
print(model_vs_accuracy)

