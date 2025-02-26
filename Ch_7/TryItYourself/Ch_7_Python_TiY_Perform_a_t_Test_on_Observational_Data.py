#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
import scipy.stats as stats

# Load the data
school_data = pd.read_csv('school.csv')

# Perform a one-sample t-test
# Null Hypothesis: The mean number of hours of sleep is 7
# Alternative Hypothesis: The mean number of hours of sleep is less than 7
t_statistic, p_value = stats.ttest_1samp(school_data['daily_sleep_hr'], 7, alternative = 'less')

# Outputting the results
print('T-statistic: ', t_statistic)
print('P-value: ', p_value)

