#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Scatter Plot ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, xlab, ggtitle, ylab, geom_smooth, ylim

# Import the data
countries = pd.read_csv('countries.csv')


# Plot the data
(ggplot(countries, aes(x = 'whr_score', y = 'ggei')) +
  geom_point() +
  geom_smooth(method = 'lm', se = False, color = 'blue') +
  ylim(0, 1) +
  xlab('World Happiness Report Score') +
  ylab('Global Green Economic Index (GGEI)') +
  ggtitle('GGEI by Score in World Happiness Report')
)

