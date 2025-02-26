#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Explore a Line Chart ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_line, xlab, ggtitle, ylab

# Import the data
child_mortality = pd.read_csv('child_mortality_long.csv')
child_mortality = child_mortality[(child_mortality['country'] == 'United States') &
                                  (child_mortality['year'] >= 1880) &
                                  (child_mortality['year'] <= 2020)]

# Plot the data
(ggplot(child_mortality, aes(x = 'year', y = 'child_mortality')) +
  geom_line() +
  xlab('Year') +
  ylab('Under-5 Mortality Rate (Deaths per 1000 Births)') +
  ggtitle('United States Child Mortality Rate over Time')
)

