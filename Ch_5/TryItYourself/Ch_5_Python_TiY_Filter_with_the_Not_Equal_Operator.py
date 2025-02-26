#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter with the Not-Equal Operator ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Filter the DataFrame for rows where 'Country' is not equal to 'Canada'
NonCanadaCustomersDf = CustomersDf[CustomersDf['Country'] != 'Canada']

# Calculate the number of observations
NumObservations = len(NonCanadaCustomersDf)

# Print the number of observations
print(f'Number of observations outside Canada: {NumObservations}')

# Filter the DataFrame for rows where 'Country' is not equal to 'Mexico'
NonMexicoCustomersDf = CustomersDf[CustomersDf['Country'] != 'Mexico']

# Calculate the number of observations
NumObservations = len(NonMexicoCustomersDf)

# Print the number of observations
print(f'Number of observations outside Mexico: {NumObservations}')

# Filter the DataFrame for rows where 'Country' is not equal to 'USA'
NonUsaCustomersDf = CustomersDf[CustomersDf['Country'] != 'USA']

# Calculate the number of observations
NumObservations = len(NonUsaCustomersDf)

# Print the number of observations
print(f'Number of observations outside the USA: {NumObservations}')

