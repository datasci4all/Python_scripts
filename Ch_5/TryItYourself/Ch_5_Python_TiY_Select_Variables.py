#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Select Variables ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Set the option to display all rows (change 1000 to your desired number)
pd.set_option('display.max_rows', 1000)

# Calculate the number of observations
NumObservations = len(CustomersDf)

# Print the number of observations
print(f'Number of observations: {NumObservations}')

# Display the 'Country' column in a tabular format
display(CustomersDf[['Country']].style.hide(axis='index'))

# Country in the 10th observatrion and city in the 10th observation
print(CustomersDf['Country'][9])
print(CustomersDf['City'][9])

