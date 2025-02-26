#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Fit, Evaluate, and Interpret Decision Trees ####

# Importing necessary libraries
import pandas as pd
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
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

# Create model piece to handle categorical variables
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['island', 'sex', 'species']),
  ],
  remainder = 'passthrough'
)

## Regression Tree (Depth 1)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=1, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_1 = r2_score(y_test, y_predicted)

## Regression Tree (Depth 3)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=3, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_2 = r2_score(y_test, y_predicted)


## Regression Tree (Depth 5)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=5, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_3 = r2_score(y_test, y_predicted)

tree.plot_tree(tree_fitted['tree'], feature_names = list(column_transformer.transform(x_train).columns),
              filled = True, fontsize = 8)

## Regression Tree (Depth 7)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=7, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_4 = r2_score(y_test, y_predicted)

## Regression Tree (Depth 10)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=10, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(x_test)

r2_5 = r2_score(y_test, y_predicted)

# From summary output above
max_depth_vs_r2 = pd.DataFrame({
    'max_depth': [1, 3, 5, 7, 10],
    'r2': [r2_1, r2_2, r2_3, r2_4, r2_5]
})

print(max_depth_vs_r2)


# In[ ]:


# Predictions for two penguins

# Create data frame for new observations
new_penguins = {'species': ['Adelie', 'Gentoo'],
            'island': ['Biscoe', 'Biscoe'],
            'bill_length_mm': [43.7, 43.7],
            'flipper_length_mm': [200, 200],
            'body_mass_g': [4160, 4160],
            'sex': ['male', 'male']}
new_penguins = pd.DataFrame(new_penguins)

# Build decision tree  model
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeRegressor(max_depth=3, ccp_alpha=0, min_samples_split=2, random_state=1234))]
).set_output(transform='pandas')


tree_fitted = tree_pipeline.fit(x_train, y_train)

y_predicted = tree_fitted.predict(new_penguins)

# Print predictions
predictions = pd.DataFrame({'species':new_penguins['species'], 'bill_depth': y_predicted})

print('Predictions for two penguins:')
print(predictions)

