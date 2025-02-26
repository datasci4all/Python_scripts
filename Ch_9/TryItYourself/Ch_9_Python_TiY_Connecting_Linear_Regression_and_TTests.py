#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Connecting Linear Regression and T-Tests ####

# Importing necessary libraries
from scipy import stats
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Import data
penguins = pd.read_csv('penguins.csv')
penguins = penguins.dropna(subset = ['bill_depth_mm', 'sex'])


bill_male = penguins['bill_depth_mm'][penguins['sex'] == 'male']
bill_female = penguins['bill_depth_mm'][penguins['sex'] == 'female']

# T-Test
print('T-Test Output:')
ttest_result = stats.ttest_ind(bill_male, bill_female)
print('T-statistic:', ttest_result.statistic, '\nP-value:', ttest_result.pvalue)


# In[ ]:


# Regression Model
penguins['is_male'] = 0
penguins.loc[penguins['sex'] == 'male','is_male'] = 1

x_train = sm.add_constant(penguins['is_male'])
y_train = penguins['bill_depth_mm']

## Traditional Linear Regression Output
print("Linear regression t-statistic:")
results = sm.OLS(y_train, x_train).fit()
print(results.tvalues.iloc[1])

print("Linear regression p-value:")
print(results.pvalues.iloc[1])

