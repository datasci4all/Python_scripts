#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Associate Two Categorical Variables ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_bar, scale_fill_manual, ggtitle, xlab, ylab, theme_minimal

# Load the dataset
videogames_df = pd.read_csv('videogames.csv')

# Filter for the specified genres
selected_genres = ['Role-Playing', 'Action', 'Sports', 'Shooter']
filtered_df = videogames_df[videogames_df['genre'].isin(selected_genres)]

# Find the top four Maturity Ratings in terms of counts
top_maturity_ratings = filtered_df['maturity_rating'].value_counts().nlargest(4).index
top_maturity_ratings_df = filtered_df[filtered_df['maturity_rating'].isin(top_maturity_ratings)]

# Define a color-blind safe palette
color_blind_palette = ['#d55e00', '#cc79a7', '#0072b2', '#f0e442']

# Plot
(ggplot(top_maturity_ratings_df, aes(x = "genre", fill = "maturity_rating")) +
  geom_bar(position = "dodge") +
  scale_fill_manual(values = color_blind_palette) +
  ggtitle('Association between Game Genre and Maturity Rating') +
  xlab('Game Genre') +
  ylab('Count') +
  theme_minimal()
)

