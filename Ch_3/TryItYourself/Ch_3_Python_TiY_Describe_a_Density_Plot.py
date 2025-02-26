#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Describe a Density Plot ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_density, xlab, ggtitle, ylab

# Import data
countries = pd.read_csv('countries.csv')

# Plot data
(ggplot(countries, aes(x = 'mean_years_of_schooling')) +
  geom_density() +
  xlab('Mean Years of Schooling') +
  ylab('Density') +
  ggtitle('Mean Years of Schooling Worldwide')
)

