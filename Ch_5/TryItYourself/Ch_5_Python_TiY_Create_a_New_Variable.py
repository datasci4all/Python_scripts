#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Create a New Variable ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
ProductsDf = pd.read_csv('Products.csv')

# Create a new DataFrame with 'Price' and a calculated column 'Price_in_Yen'
YenConversionRate = 142
ProductsDf['PriceInYen'] = ProductsDf['Price'] * YenConversionRate

# Set the option to display all rows (change 1000 to your desired number)
pd.set_option('display.max_rows', 1000)

# Display the resulting DataFrame
display(ProductsDf.style.hide(axis='index'))

