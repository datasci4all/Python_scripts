#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Compare Regression Models ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

# Import data
penguins_train = pd.read_csv('penguins_train.csv')
penguins_train = penguins_train.dropna()

penguins_test = pd.read_csv('penguins_test.csv')
penguins_test = penguins_test.dropna()

# Distinguish training and test data
x_train = penguins_train.drop('bill_depth_mm', axis=1)
y_train = penguins_train['bill_depth_mm']

x_test = penguins_test.drop('bill_depth_mm', axis=1)
y_test = penguins_test['bill_depth_mm']

# Model piece for dealing with categorical variables
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['island', 'sex', 'species']),
  ],
  remainder = 'passthrough'
)

## Linear Regression with all explanatory variables
linear_pipeline = Pipeline(
  [('preprocessing', column_transformer),
   ('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

linear_fitted = linear_pipeline.fit(x_train, y_train)

y_predicted = linear_fitted.predict(x_test)
r2_1 = r2_score(y_test, y_predicted)

## Decision Tree with Max Depth of 10
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=10))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_2 = r2_score(y_test, y_predicted)

## Random Forest with Min n of 15
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=15))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_3 = r2_score(y_test, y_predicted)


## kNN with k = 10
knn_pipeline = Pipeline(
  [('preprocessing', column_transformer),
   ('knn', KNeighborsRegressor(n_neighbors=10))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(x_train, y_train)

y_predicted = knn_pipeline.predict(x_test)

r2_4 = r2_score(y_test, y_predicted)

# From summary output above
method_vs_r2 = pd.DataFrame(
    {'method': ['Multiple Linear Regression', 'Decision Tree', 'Random Forest', 'kNN'], 'r2': [r2_1, r2_2, r2_3, r2_4]}
)

print(method_vs_r2)

