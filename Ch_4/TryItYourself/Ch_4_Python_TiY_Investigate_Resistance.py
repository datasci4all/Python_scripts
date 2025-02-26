#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Investigate Resistance ####

# Importing necessary libraries
import pandas as pd
from scipy import stats

# Load the dataset
linkedin_df = pd.read_csv('linkedin_connections.csv')

# Calculating various statistics for 'LinkedIn_connections'
mean_linkedin_connections = linkedin_df['linkedin_connections'].mean()
trimmed_mean_linkedin_connections = stats.trim_mean(linkedin_df['linkedin_connections'], 0.1)
median_linkedin_connections = linkedin_df['linkedin_connections'].median()
range_linkedin_connections = linkedin_df['linkedin_connections'].max() - linkedin_df['linkedin_connections'].min()
variance_linkedin_connections = linkedin_df['linkedin_connections'].var()
std_dev_linkedin_connections = linkedin_df['linkedin_connections'].std()

# Creating a table to display the results
summary_stats = pd.DataFrame({
    'Statistic': ['Mean', '80% Trimmed Mean', 'Median', 'Range', 'Variance', 'Standard Deviation'],
    'Value': [mean_linkedin_connections,
              trimmed_mean_linkedin_connections,
              median_linkedin_connections,
              range_linkedin_connections,
              variance_linkedin_connections,
              std_dev_linkedin_connections]
})

print(summary_stats)

