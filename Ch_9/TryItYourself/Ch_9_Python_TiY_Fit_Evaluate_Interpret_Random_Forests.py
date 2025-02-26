#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Fit, Evaluate, Interpret Random Forests ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
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

# Create model piece for handling
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['island', 'sex', 'species']),
  ],
  remainder = 'passthrough'
)

## Regression RF (Min n = 30)
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=30, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_1 = r2_score(y_test, y_predicted)

importances = forest_fitted['rf'].feature_importances_
forest_importances = pd.DataFrame({
    'Variable Importance': importances,
    'Variable': column_transformer.transform(x_train).columns
})
forest_importances = forest_importances.sort_values(['Variable Importance'], ascending=False)
print('Variable Importances for model with Min n of 30:')
print(forest_importances)

## Regression RF (Min n = 20)
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=20, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_2 = r2_score(y_test, y_predicted)


## Regression RF (Min n = 15)
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=15, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_3 = r2_score(y_test, y_predicted)

## Regression RF (Min n = 10)
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=10, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_4 = r2_score(y_test, y_predicted)

## Regression RF (Min n = 5)
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=5, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

y_predicted = forest_fitted.predict(x_test)

r2_5 = r2_score(y_test, y_predicted)

# From summary output above
min_n_vs_r2 = pd.DataFrame(
    {'min_n': [30, 20, 15, 10, 5], 'r2': [r2_1, r2_2, r2_3, r2_4, r2_5]}
)

print(min_n_vs_r2)


# In[ ]:


# Predictions for two penguins

# Create data frame for new observations
new_penguins = {'species': ['Adelie', 'Adelie'],
            'island': ['Biscoe', 'Biscoe'],
            'bill_length_mm': [43.7, 43.7],
            'flipper_length_mm': [200, 242],
            'body_mass_g': [4160, 4160],
            'sex': ['male', 'male']}
new_penguins = pd.DataFrame(data = new_penguins)

# Fit decision tree model
forest_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('rf', RandomForestRegressor(min_samples_split=30, random_state=1234))]
).set_output(transform='pandas')


forest_fitted = forest_pipeline.fit(x_train, y_train)

# Print predictions
y_predicted = forest_fitted.predict(new_penguins)
predictions = pd.DataFrame({'flipper_length_mm':new_penguins['flipper_length_mm'], 'bill_depth': y_predicted})

print("Predictions for two penguins:")
print(predictions)

