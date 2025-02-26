#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter Text Variables ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Filter the DataFrame for rows where 'Country' is equal to 'Mexico'
MexicoCustomersDf = CustomersDf[CustomersDf['Country'] == 'Mexico']

# Calculate the number of observations
NumObservations = len(MexicoCustomersDf)

# Print the number of observations
print(f'Number of observations in Mexico: {NumObservations}')

# Display the resulting DataFrame with all columns
display(MexicoCustomersDf.style.hide(axis = 'index'))


# Filter the DataFrame for rows where 'Country' is equal to 'USA'
UsaCustomersDf = CustomersDf[CustomersDf['Country'] == 'USA']

# Calculate the number of observations
NumObservations = len(UsaCustomersDf)

# Print the number of observations
print(f'Number of observations in the USA: {NumObservations}')

# Display the resulting DataFrame with all columns
display(UsaCustomersDf.style.hide(axis = 'index'))

