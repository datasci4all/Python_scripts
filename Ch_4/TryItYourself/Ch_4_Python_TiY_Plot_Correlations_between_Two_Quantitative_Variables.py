#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Plot Correlations between Two Quantitative Variables ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_smooth, annotate, labs, theme_bw

# Load the dataset
videogames_df = pd.read_csv('videogames.csv')

# Calculate the correlation coefficient
corr_coefficient = videogames_df[['critic_rating', 'user_rating']].corr().iloc[0, 1]

# Create a scatterplot with a regression line
(ggplot(videogames_df, aes(x="critic_rating", y="user_rating")) +
  geom_point() +
  geom_smooth(method='lm', color='red', se=False) +
  annotate('text', x=videogames_df['critic_rating'].min(), y=videogames_df['user_rating'].max(), label=f'Corr: {corr_coefficient:.2f}', size=7) +
  labs(title='Scatterplot of Critic_Rating and User_Rating') +
  theme_bw(base_size = 14)
)


# In[ ]:


# Calculate the correlation coefficient
corr_coefficient = videogames_df[['user_count', 'user_rating']].corr().iloc[0, 1]

# Create a scatterplot with a regression line
(ggplot(videogames_df, aes(x="user_count", y="user_rating")) +
  geom_point() +
  geom_smooth(method='lm', color='red', se=False) +
  annotate('text', x=videogames_df['user_count'].max(), y=videogames_df['user_rating'].min(), label=f'Corr: {corr_coefficient:.2f}', size=7) +
  labs(title='Scatterplot of User_Count and User_Rating') +
  theme_bw(base_size = 16)
)

