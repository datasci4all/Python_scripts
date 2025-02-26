#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Clean Incorrect Formats ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
data = pd.read_csv('vote.csv')

# Count the initial number of 'dog' and 'cat' responses before cleaning
initial_dog_count = data['favorite_pet'].eq('dog').sum()
initial_cat_count = data['favorite_pet'].eq('cat').sum()

# Clean the data
data['favorite_pet'] = data['favorite_pet'].replace(
    {
        r'dogs': 'dog',  # Replace 'dogs' with 'dog'
        r'cats': 'cat',  # Replace 'cats' with 'cat'
        r'd.*g': 'dog',  # Replace words starting with d and ending with g with 'dog'
        r'c.*t': 'cat'   # Replace words starting with c and ending with t with 'cat'
    }, regex=True)

# Count the number of 'dog' and 'cat' responses after cleaning
final_dog_count = data['favorite_pet'].eq('dog').sum()
final_cat_count = data['favorite_pet'].eq('cat').sum()

print(f"Initial dog count: {initial_dog_count}")
print(f"Initial cat count: {initial_cat_count}")
print(f"Final dog count: {final_dog_count}")
print(f"Final cat count: {final_cat_count}")

