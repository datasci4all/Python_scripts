#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Describe a Bubble Chart ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, xlab, ggtitle, ylab, labs, theme, ylim

# Import the data
countries = pd.read_csv('countries.csv')

# Plot the data
(ggplot(countries, aes(x = 'prop_internet', y = 'ggei', size = 'gni_per_capita')) +
  geom_point(color = 'blue', alpha = .75) +
  ylim(0, 1) +
  xlab('Proportion of People in\nCountry with Internet Access') +
  ylab('Global Green Economic Index (GGEI)') +
  labs(size = 'Gross National Income (GNI)\nper Capita') +
  ggtitle('GGEI by Proportion of People\nwith Internet Access') +
  theme(figure_size=(12, 8))
)

