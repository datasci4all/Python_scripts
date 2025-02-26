#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Calculate the Range, Variance, and Standard Deviation ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
videogames_df = pd.read_csv('videogames.csv')

# Calculating range, variance, and standard deviation for 'User_Rating'
range_user_rating = videogames_df['user_rating'].max() - videogames_df['user_rating'].min()
variance_user_rating = videogames_df['user_rating'].var()
std_dev_user_rating = videogames_df['user_rating'].std()

# Output the calculated values
print('Range of User Rating:', range_user_rating)
print('Variance of User Rating:', variance_user_rating)
print('Standard Deviation of User Rating:', std_dev_user_rating)

