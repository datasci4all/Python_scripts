#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Contemplate a Box Plot with a Categorical Variable ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_boxplot, xlab, ggtitle, ylab

# Import the data
countries = pd.read_csv('countries.csv')
continents = ['Africa', 'Asia', 'Oceania']
countries = countries[countries['continent'].isin(continents)]

# Plot the data
(ggplot(countries, aes(x = 'continent', y = 'life_expectancy', fill = 'continent')) +
  geom_boxplot() +
  xlab('Continent') +
  ylab('Mean Life Expectancy') +
  ggtitle('Mean Life Expectancies by Continent')
)

