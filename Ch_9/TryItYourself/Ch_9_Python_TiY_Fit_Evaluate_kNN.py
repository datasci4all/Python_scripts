#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Fit and Evaluate k-Nearest Neighbors ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Import data
penguins_train = pd.read_csv('penguins_train.csv')
penguins_train = penguins_train.dropna()

penguins_test = pd.read_csv('penguins_test.csv')
penguins_test = penguins_test.dropna()


# Distinguish
X_train = penguins_train[['bill_length_mm']]
y_train = penguins_train['bill_depth_mm']

X_test = penguins_test[['bill_length_mm']]
y_test = penguins_test['bill_depth_mm']

## Regression kNN (k = 1)
knn_pipeline = Pipeline(
  [('knn', KNeighborsRegressor(n_neighbors=1, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(X_train, y_train)

y_predicted = knn_fitted.predict(X_test)

r2_1 = r2_score(y_test, y_predicted)


## Regression kNN (k = 3)
knn_pipeline = Pipeline(
  [('knn', KNeighborsRegressor(n_neighbors=3, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(X_train, y_train)

y_predicted = knn_pipeline.predict(X_test)

r2_2 = r2_score(y_test, y_predicted)



## Regression kNN (k = 5)
knn_pipeline = Pipeline(
  [('knn', KNeighborsRegressor(n_neighbors=5, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(X_train, y_train)

y_predicted = knn_pipeline.predict(X_test)

r2_3 = r2_score(y_test, y_predicted)

## Regression kNN (k = 10)
knn_pipeline = Pipeline(
  [('knn', KNeighborsRegressor(n_neighbors=10, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(X_train, y_train)

y_predicted = knn_pipeline.predict(X_test)

r2_4 = r2_score(y_test, y_predicted)


## Regression kNN (k = 25)
knn_pipeline = Pipeline(
  [('knn', KNeighborsRegressor(n_neighbors=25, p = 2))]
).set_output(transform='pandas')

knn_fitted = knn_pipeline.fit(X_train, y_train)

y_predicted = knn_pipeline.predict(X_test)

r2_5 = r2_score(y_test, y_predicted)

# From summary output above
k_vs_r2 = pd.DataFrame(
    {'k': [1, 3, 5, 10, 25], 'r2': [r2_1, r2_2, r2_3, r2_4, r2_5]}
)

print(k_vs_r2)

