#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Calculate Mean, Mode, Median, and 90% Trimmed Mean ####

# Importing necessary libraries
import pandas
from scipy.stats import trim_mean

# Reading the data into a DataFrame
videogames = pandas.read_csv('videogames.csv')

# Calculating mean, median, mode, and trimmed mean for 'User_Score'
mean_rating = videogames['user_rating'].mean()
median_rating = videogames['user_rating'].median()
mode_rating = videogames['user_rating'].mode()[0]
mean_90_rating = trim_mean(videogames['user_rating'], proportiontocut=0.05)

# Creating a DataFrame to display the calculated statistics
summary = pandas.DataFrame([{
    'Mean Rating': mean_rating,
    '90% Trimmed Mean Rating': mean_90_rating,
    'Median Rating': median_rating,
    'Mode Rating': mode_rating
}])

# Displaying the summary DataFrame
print(summary)

