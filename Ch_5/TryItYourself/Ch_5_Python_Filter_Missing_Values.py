#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter Missing Values ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Filter the DataFrame for rows where 'PostalCode' is missing (NaN or None)
FilteredCustomersMissingPostalcode = CustomersDf[CustomersDf['PostalCode'].isnull()]

# Calculate the number of observations
NumObservations = len(FilteredCustomersMissingPostalcode)

# Print the number of observations
print(f'Number of observations where PostalCode is null: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredCustomersMissingPostalcode.style.hide(axis = 'index'))

