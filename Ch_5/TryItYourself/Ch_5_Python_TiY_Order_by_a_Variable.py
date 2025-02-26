#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Order by a Variable ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
ProductsDf = pd.read_csv('Products.csv')

# Sort the DataFrame by 'Price' in ascending order
SortedProducts = ProductsDf.sort_values(by='Price', ascending=True)

# Calculate the number of observations
NumObservations = len(SortedProducts)

# Print the number of observations
print(f'Number of observations: {NumObservations}')

# Display the resulting DataFrame with all columns
display(SortedProducts.style.hide(axis = 'index'))


# Sort and Display the DataFrame by 'Price' in descending order
SortedProducts = ProductsDf.sort_values(by='Price', ascending=False)
display(SortedProducts.style.hide(axis = "index"))

