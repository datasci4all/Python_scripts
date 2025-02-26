#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Violin Plot ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_density, xlab, ylab, ggtitle, geom_violin, geom_boxplot, scale_x_continuous, theme

def no_labels(values):
    return [''] * len(values)

# Import data
countries = pd.read_csv('countries.csv')

# Plot the data
(ggplot(countries, aes(x = 1, y = 'under_5_mortality_rate')) +
  geom_violin(color = 'black', fill = 'salmon') +
  geom_boxplot(width = 0.1) +
  xlab('') +
  ylab('Under-5 Mortality Rate (Deaths per 1000 Births)') +
  scale_x_continuous(labels=no_labels) +
  ggtitle('Worldwide Distribution of Mortality Rate for Children Under 5') +
  theme(figure_size=(8, 6))
)

