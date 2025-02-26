#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter a Quantitative Variable ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
ProductsDf = pd.read_csv('Products.csv')

# Filter the DataFrame for rows where 'Price' is greater than or equal to 45
FilteredProducts45Df = ProductsDf[ProductsDf['Price'] >= 45]

# Calculate the number of observations
NumObservations = len(FilteredProducts45Df)

# Print the number of observations
print(f'Number of observations where the Price >= $45: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredProducts45Df.style.hide(axis = 'index'))

# Add a few blank lines
print('\n\n')



# Filter the DataFrame for rows where 'Price' is less than 10
FilteredProducts10Df = ProductsDf[ProductsDf['Price'] < 10]

# Calculate the number of observations
NumObservations = len(FilteredProducts10Df)

# Print the number of observations
print(f'Number of observations where the Price < $10: {NumObservations}')

# Display the resulting DataFrame with all columns
display(FilteredProducts10Df.style.hide(axis = 'index'))


