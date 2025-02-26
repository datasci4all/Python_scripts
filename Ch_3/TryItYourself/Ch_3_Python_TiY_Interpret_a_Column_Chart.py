#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Column Chart ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_col, xlab, ggtitle, geom_text, ylab, labs

# Import the data
countries = pd.read_csv('countries.csv')

# Compute means
internet_means = pd.DataFrame(countries.groupby('continent')['prop_internet'].mean()).round(2).reset_index()

# Plot the data
(ggplot(internet_means, aes(x = 'continent', y = 'prop_internet', fill = 'continent')) +
  geom_col() +
  geom_text(aes(label = internet_means['prop_internet']), nudge_y = 5) +
  xlab('Continent') +
  ylab('Mean Percentage Among Countries') +
  labs(fill = 'Continent') +
  ggtitle('Mean Percentage of People with Internet Access by Continent')
)

