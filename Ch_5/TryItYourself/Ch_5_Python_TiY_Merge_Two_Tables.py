#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Merge Two Tables ####

# Importing necessary libraries
import pandas as pd

# Load the CSV files into DataFrames (replace with your file paths)
CustomersDf = pd.read_csv('Customers.csv')
OrdersDf = pd.read_csv('Orders.csv')

# Perform an inner join between 'Customers' and 'Orders' on 'CustomerID'
ResultDf = pd.merge(CustomersDf[['CustomerID', 'CustomerName']], OrdersDf[['CustomerID', 'OrderDate']], on='CustomerID', how='inner')

# Set the option to display all rows
pd.set_option('display.max_rows', 1000)

# Calculate the number of observations
NumObservations = len(ResultDf)

# Print the number of observations
print(f'Number of observations: {NumObservations}')

# Display the resulting DataFrame with only 'CustomerName' and 'OrderDate' columns
display(ResultDf[['CustomerID', 'CustomerName', 'OrderDate']].style.hide(axis='index'))

