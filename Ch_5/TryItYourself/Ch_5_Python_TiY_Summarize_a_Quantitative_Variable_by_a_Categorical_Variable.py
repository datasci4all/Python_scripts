#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Summarize a Quantitative Variable by a Categorical Variable ####

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
ProductsDf = pd.read_csv('Products.csv')

# Group the DataFrame by 'CategoryID' and calculate the average price for each group
AveragePriceByCategory = ProductsDf.groupby('CategoryID')['Price'].agg('mean')

# Reset the index to have 'CategoryID' as a column in the result
AveragePriceByCategory = AveragePriceByCategory.reset_index()

# Rename the columns to match the SQL query
AveragePriceByCategory.columns = ['CategoryID', 'AveragePrice']

# Display the resulting DataFrame
display(AveragePriceByCategory.style.hide(axis = 'index'))

