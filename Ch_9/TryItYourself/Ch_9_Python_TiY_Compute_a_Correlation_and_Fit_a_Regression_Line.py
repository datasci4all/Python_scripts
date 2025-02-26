#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Compute a Correlation and Fit a Regression Line ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_smooth
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import numpy as np

# Import data
penguins = pd.read_csv('penguins.csv')
penguins = penguins.dropna(subset = ['bill_depth_mm', 'flipper_length_mm'])

# Plot the data
(ggplot(penguins, aes(x = 'flipper_length_mm', y = 'bill_depth_mm')) +
  geom_point() +
  geom_smooth(method = 'lm', se = False)
)


# In[ ]:


# Compute and print correlation
correlation = np.corrcoef(penguins['bill_depth_mm'], penguins['flipper_length_mm'])
print('Correlation:', correlation[0][1])


# In[ ]:


# Fit regression model
regression_pipeline = Pipeline(
  [('lr', LinearRegression(fit_intercept = True))]
).set_output(transform='pandas')

x_train = pd.DataFrame(penguins['flipper_length_mm'])
y_train = penguins['bill_depth_mm']
regression_fitted = regression_pipeline.fit(x_train, y_train)

regression_slope = regression_fitted['lr'].coef_[0]
print('Linear Regression Slope Coefficient:', regression_slope)

