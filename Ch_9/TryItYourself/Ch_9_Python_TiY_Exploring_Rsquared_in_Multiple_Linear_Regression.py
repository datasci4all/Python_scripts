#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Multiple Linear Regression ####

# Importing necessary libraries
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from plotnine import ggplot, aes, geom_point, xlab, ylab, ggtitle

# Import data
penguins = pd.read_csv('penguins.csv')
penguins = penguins.dropna(subset = ['bill_depth_mm', 'body_mass_g', 'species', 'bill_length_mm', 'flipper_length_mm', 'sex'])

# Build regression model pieces
column_transformer_1 = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['species']),
  ],
  remainder = 'passthrough'
)

column_transformer_2 = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['species', 'sex']),
  ],
  remainder = 'passthrough'
)

regression_pipeline_1 = Pipeline(
  [('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

regression_pipeline_2 = Pipeline(
  [('preprocessing', column_transformer_1),
   ('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

regression_pipeline_3 = Pipeline(
  [('preprocessing', column_transformer_2),
   ('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

y_train = penguins['bill_depth_mm']

## Traditional Linear Regression 1
x_train = pd.DataFrame(penguins['body_mass_g'])
regression_fitted = regression_pipeline_1.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_train)
r2_1 = r2_score(y_train, y_predicted)

slope = regression_fitted["lr"].coef_[0]
print('The estimated slope coefficient in model 1:', slope)


# In[ ]:


## Traditional Linear Regression 2
x_train = pd.DataFrame(penguins[['body_mass_g', 'species']])
regression_fitted = regression_pipeline_2.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_train)
r2_2 = r2_score(y_train, y_predicted)

## Traditional Linear Regression 3
x_train = pd.DataFrame(penguins[['body_mass_g', 'species', 'bill_length_mm']])
regression_fitted = regression_pipeline_2.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_train)
r2_3 = r2_score(y_train, y_predicted)

## Traditional Linear Regression 4
x_train = pd.DataFrame(penguins[['body_mass_g', 'species', 'bill_length_mm', 'flipper_length_mm']])
regression_fitted = regression_pipeline_2.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_train)
r2_4 = r2_score(y_train, y_predicted)

## Traditional Linear Regression 5
x_train = pd.DataFrame(penguins[['body_mass_g', 'species', 'bill_length_mm', 'flipper_length_mm', 'sex']])
regression_fitted = regression_pipeline_3.fit(x_train, y_train)

y_pred = regression_fitted.predict(x_train)
r2_5 = r2_score(y_train, y_predicted)

# From summary output above
d = {'num_vars': [1, 2, 3, 4, 5], 'r2': [r2_1, r2_2, r2_3, r2_4, r2_5] }
results = pd.DataFrame(d)

# Plot results
(ggplot(results, aes(x = 'num_vars', y = 'r2')) +
  geom_point(size = 4) +
  xlab('Number of Explanatory Variables') +
  ylab('R-squared') +
  ggtitle('R-Squared vs.\nNumber of Explanatory Variables')
)

