#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Identify Extreme Data Values

# Importing necessary libraries
import pandas as pd

# Load the data
data = pd.read_csv('vote.csv')

# Calculate the 5th and 95th percentiles of age
age_5th_percentile = data['age'].quantile(0.05)
age_95th_percentile = data['age'].quantile(0.95)

# Get the range of the oldest 5% and youngest 5% of respondents
oldest_5_percent_range = data[data['age'] >= age_95th_percentile]['age'].agg(['min', 'max'])
youngest_5_percent_range = data[data['age'] <= age_5th_percentile]['age'].agg(['min', 'max'])

# Count the number of respondents above 100 and below 18
above_100_count = data[data['age'] > 100].shape[0]
below_18_count = data[data['age'] < 18].shape[0]

print('Highest age of the lowest 5%:', age_5th_percentile)
print('Lowest age of the highest 5%:', age_95th_percentile)
print('Oldest 5% age range:', oldest_5_percent_range)
print('Youngest 5% age range:', youngest_5_percent_range)
print('Number of respondents above 100:', above_100_count)
print('Number of respondents below 18:', below_18_count)

