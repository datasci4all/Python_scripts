#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Select Distinct Values of Variables

# Importing necessary libraries
import pandas as pd

# Load the CSV file into a DataFrame
CustomersDf = pd.read_csv('Customers.csv')

# Get unique/distinct values from the 'Country' column
UniqueCountries = CustomersDf['Country'].unique()

# Set the option to display all rows (change 1000 to your desired number)
pd.set_option('display.max_rows', 1000)

# Calculate the number of unique observations
NumUniqueCountries = len(UniqueCountries)

# Print the number of unique observations
print(f'Number of unique observations: {NumUniqueCountries}')

# Convert the array of unique countries back into a DataFrame for display
UniqueCountriesDf = pd.DataFrame(UniqueCountries, columns=['Country'])

# Display the DataFrame
display(UniqueCountriesDf.style.hide(axis='index'))


