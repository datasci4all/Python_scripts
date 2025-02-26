#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Extrapolation ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Create data frame for data in text
age = pd.DataFrame([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
height = [42, 45, 48, 51, 54.5, 58, 61,
            63.5, 66, 68.5, 69.5, 70, 71, 71.5, 72]

# Fit regression model
regression_pipeline = Pipeline(
  [('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(age, height)
[regression_fitted['lr'].intercept_, regression_fitted['lr'].coef_]

# Extract the Linear Regression model from the pipeline
model = regression_fitted.named_steps['lr']

# Get the coefficient for 'age'
coefficient = model.coef_

# Get the intercept
intercept = model.intercept_

print('Coefficient (slope) for age:', coefficient[0])
print('Intercept:', intercept)


# In[ ]:


# Make prediction
new_age = pd.DataFrame([40])

new_height = float(regression_fitted.predict(new_age)[0])
print('Prediction for Height at Age 40:', new_height)

