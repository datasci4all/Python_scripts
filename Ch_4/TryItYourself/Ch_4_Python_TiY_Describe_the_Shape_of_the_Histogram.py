#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Describe the Shape of the Histogram ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_histogram, theme_minimal, labs

# Load the dataset
videogames_df = pd.read_csv('videogames.csv')

# Plotting a histogram of User_Ratings
(ggplot(videogames_df, aes(x = 'user_rating')) +
  geom_histogram(bins = 30, binwidth = 0.3233, boundary =0, fill = "#0072b2", color = "black") +
  theme_minimal() +
  labs(title = 'Histogram of User Ratings',
       x = 'User Rating',
       y = 'Frequency')
)

