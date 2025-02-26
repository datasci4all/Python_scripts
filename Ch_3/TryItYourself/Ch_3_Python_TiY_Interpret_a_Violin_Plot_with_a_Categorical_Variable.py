#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Violin Plot with a Categorical variable ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_boxplot, xlab, ggtitle, ylab, geom_violin, labs

# Import the data
countries = pd.read_csv('countries.csv')
incomes = ['Lower middle income', 'Upper middle income']
countries = countries[countries['income_group'].isin(incomes)]

# Plot the data
(ggplot(countries, aes(x = 'income_group', y = 'gni_per_capita', fill = 'income_group')) +
  geom_violin() +
  geom_boxplot(fill = 'white', width = 0.1) +
  xlab('Income Group') +
  ylab('GNI per Capita') +
  labs(fill = 'Income Group') +
  ggtitle('GNI per Capita Among Lower Middle and\nUpper Middle Income Groups')
)

