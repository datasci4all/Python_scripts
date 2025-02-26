#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter Using a Wildcard ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Filter the DataFrame for rows where 'ContactName' starts with 'Z'
FilteredCustomersDfZ = CustomersDf[CustomersDf['ContactName'].str.startswith('Z')]

# Calculate the number of observations
NumObservations = len(FilteredCustomersDfZ)

# Print the number of observations
print(f'Number of observations where ContactName starts with a Z: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredCustomersDfZ.style.hide(axis = 'index'))

# Add a few blank lines
print('\n\n')

# Filter the DataFrame for rows where 'CustomerName' starts with 'B'
FilteredCustomersDfStartB = CustomersDf[CustomersDf['CustomerName'].str.startswith('B')]

# Calculate the number of observations
NumObservations = len(FilteredCustomersDfStartB)

# Print the number of observations
print(f'Number of observations where CustomerName starts with a B: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredCustomersDfStartB.style.hide(axis = 'index'))


# Add a few blank lines
print('\n\n')

# Filter the DataFrame for rows where 'CustomerName' ends with 'B'
FilteredCustomersDfEndB = CustomersDf[CustomersDf['CustomerName'].str.endswith('B')]

# Calculate the number of observations
NumObservations = len(FilteredCustomersDfEndB)

# Print the number of observations
print(f'Number of observations where CustomerName ends with a B: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredCustomersDfEndB.style.hide(axis = 'index'))

