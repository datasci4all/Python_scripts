#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Work with a Boxplot ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_boxplot, ylab, ggtitle, xlab, scale_x_continuous

def no_labels(values):
    return [''] * len(values)

# Import data
countries = pd.read_csv('countries.csv')

# Plot the data
(ggplot(countries, aes(x = 1, y = 'whr_score')) +
  geom_boxplot(fill = 'purple', color = 'black') +
  ylab('WHR Score') +
  xlab('') +
  scale_x_continuous(labels=no_labels) +
  ggtitle('Distribution of World Happiness Report (WHR) Scores Worldwide')
)

