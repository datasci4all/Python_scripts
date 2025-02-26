#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
import scipy.stats as stats

# Load the data
school_data = pd.read_csv('school.csv')

# Perform a one-sample t-test
# Null Hypothesis: The mean number of GPA is 3.5
# Alternative Hypothesis: The mean GPA is less than 3.5
t_statistic, p_value = stats.ttest_1samp(school_data['gpa'], 3.5, alternative = 'less')

# Outputting the results
print('T-statistic: ', t_statistic)
print('P-value: ', p_value)

