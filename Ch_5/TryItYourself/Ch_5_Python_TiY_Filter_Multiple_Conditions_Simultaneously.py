#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Filter Multiple Conditions Simultaneously

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
products_df = pd.read_csv('Products.csv')

# Filter the DataFrame for rows where 'Unit' is "24 - 12 oz bottles" and 'Price' is 19
filtered_products_df = products_df[(products_df['Unit'] == '24 - 12 oz bottles') & (products_df['Price'] == 19)]

# Calculate the number of observations
num_observations = len(filtered_products_df)

# Print the number of observations
print(f"Number of observations where Unit is '24 - 12 oz bottles' and Price = 19: {num_observations}")

# Display the resulting DataFrame with all columns
display(filtered_products_df.style.hide(axis = "index"))

# Add a few blank lines
print("\n\n")


# Filter the DataFrame for rows where 'Unit' is "24 - 12 oz bottles" and 'Price' is 14
filtered_products_df2 = products_df[(products_df['Unit'] == '24 - 12 oz bottles') & (products_df['Price'] == 14)]

# Calculate the number of observations
num_observations = len(filtered_products_df2)

# Print the number of observations
print(f"Number of observations where Unit is '24 - 12 oz bottles' and Price = 14: {num_observations}")

# Display the resulting DataFrame with all columns
display(filtered_products_df2.style.hide(axis = "index"))

# Add a few blank lines
print("\n\n")


# Filter the DataFrame for rows where 'Unit' is "24 - 12 oz bottles" and 'Price' is at least 10
filtered_products_df2 = products_df[(products_df['Unit'] == '24 - 12 oz bottles') & (products_df['Price'] >= 10)]

# Calculate the number of unique observations
num_observations = len(filtered_products_df2)

# Print the number of unique observations
print(f"Number of observations where Unit is '24 - 12 oz bottles' and Price >= 10: {num_observations}")

# Display the resulting DataFrame with all columns
display(filtered_products_df2.style.hide(axis = "index"))


