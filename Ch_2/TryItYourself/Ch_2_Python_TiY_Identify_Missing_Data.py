#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Identify Missing Data ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
data = pd.read_csv('vote.csv')

# Count the number of missing values in GPA
missing_gpa = data['gpa'].isnull().sum()

# Count the total number of rows in the dataset
total_rows = data.shape[0]

# Calculate the percentage of missing GPA values
percentage_missing_gpa = (missing_gpa / total_rows) * 100

# Display the results
print(f'Number of missing GPA values: {missing_gpa}')
print(f'Total number of rows: {total_rows}')
print(f'Percentage of missing GPA values: {percentage_missing_gpa:f}%')

