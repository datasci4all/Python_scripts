#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Perform a Two-Sample T-Test ####

# Importing necessary libraries
from scipy import stats
import pandas as pd
import numpy as np

# Import data
penguin_flipper_length = pd.read_csv('penguins_flipper_sex.csv')

flipper_length_male = penguin_flipper_length['flipper_length_male']
flipper_length_female = penguin_flipper_length['flipper_length_female']

# Perform the T-test
ttest_result = stats.ttest_ind(flipper_length_female, flipper_length_male, nan_policy='omit')

# Manually format the output to avoid scientific notation
t_statistic = ttest_result.statistic
p_value = ttest_result.pvalue

print('T-Test Output:', '\nT-statistic:', t_statistic, '\nP-value:', p_value)


# In[ ]:


# Compute and print means
print('Male Mean of Flipper Length:')
print(flipper_length_male.mean())

print('Female Mean of Flipper Length:')
print(flipper_length_female.mean())

