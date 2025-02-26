#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Create a Boolean Variable that Represents a Categorical Variable ####

# Importing necessary libraries
import pandas as pd

# Load the data
data = pd.read_csv('vote.csv')

# Create drinking_age variable
data['drinking_age'] = 0
data.loc[data['age'] >= 21, 'drinking_age'] = 1

# Count the number of 1s and 0s in drinking_age
drinking_age_counts = data['drinking_age'].value_counts()
print('Drinking Age Counts:\n', drinking_age_counts)

# Count the number of people who voted based on drinking age
voted_drinking_age = data[data['drinking_age'] == 1]['voted'].sum()
voted_non_drinking_age = data[data['drinking_age'] == 0]['voted'].sum()
print('Number of people of drinking age who voted:', voted_drinking_age)
print('Number of people not of drinking age who voted:', voted_non_drinking_age)

# Calculate the percentages
percentage_drinking_age = voted_drinking_age / drinking_age_counts[1] * 100
percentage_non_drinking_age = voted_non_drinking_age / drinking_age_counts[0] * 100
print('Percentage of drinking age people who voted:', percentage_drinking_age, '%')
print('Percentage of non-drinking age people who voted:', percentage_non_drinking_age, '%')

