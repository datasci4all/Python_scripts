#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Impute Missing Values from Internal Data ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
data = pd.read_csv('vote.csv')

# Calculate mean and median GPA before imputation
mean_gpa_before = data['gpa'].mean()
median_gpa_before = data['gpa'].median()

# Perform mean imputation for missing GPA values
mean_imputation_value = data['gpa'].mean()
data['gpa_imputed'] = data['gpa'].fillna(mean_imputation_value)

# Calculate mean and median GPA after imputation
mean_gpa_after = data['gpa_imputed'].mean()
median_gpa_after = data['gpa_imputed'].median()

# Display the results
print('Mean GPA before imputation:', mean_gpa_before)
print('Median GPA before imputation:', median_gpa_before)
print('Mean GPA after imputation:', mean_gpa_after)
print('Median GPA after imputation:', median_gpa_after)

