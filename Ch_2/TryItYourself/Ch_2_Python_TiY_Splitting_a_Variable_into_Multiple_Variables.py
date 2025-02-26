#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Splitting a Variable into Multiple Variables ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
data = pd.read_csv('vote.csv')

# Separate 'Birthdate' column into two columns for month and day
data[['day', 'month']] = data['birthdate'].str.split('-', n = 2, expand = True)

# Count the number of people per birth month
birth_month_counts = data['month'].value_counts().sort_index()

# Display the birth month counts
print(birth_month_counts.to_string())

