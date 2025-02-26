#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Summarize a Quantitative Variable ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
ProductsDf = pd.read_csv('Products.csv')

# Calculate the average price
MeanPrice = ProductsDf['Price'].mean()

# Print the formatted result
print(f'Mean Price: {round(MeanPrice, 2)}')

# Calculate the average price
MaxPrice = ProductsDf['Price'].max()

# Print the formatted result
print(f'Maximum Price: {MaxPrice}')

# Calculate the average price
MinPrice = ProductsDf['Price'].min()

# Print the formatted result
print(f'Minimum Price: {MinPrice}')

