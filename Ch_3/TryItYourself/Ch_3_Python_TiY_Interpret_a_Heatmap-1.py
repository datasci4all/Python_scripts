#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Heatmap ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_tile, xlab, ggtitle, ylab, geom_text, scale_fill_gradient, labs, theme

# Import the data
countries = pd.read_csv('countries.csv')

incomes = ['High income', 'Upper middle income',
                             'Lower middle income']
country_names = ['Vanuatu', 'Tonga', 'Solomon Islands', 'Samoa',
                        'Papua New Guinea', 'New Zealand', 'Micronesia',
                        'Fiji', 'Australia']
countries = countries[countries['income_group'].isin(incomes)]
countries = countries[countries['country'].isin(country_names)]

income_order = pd.Categorical(countries['income_group'], categories=['High income', 'Upper middle income',
                                                                    'Lower middle income'])
countries = countries.assign(income_order = income_order)

# Plot the data
(ggplot(countries, aes(x = 'income_order', y = 'country', fill = 'under_5_mortality_rate')) +
  geom_tile() +
  geom_text(aes(label = 'under_5_mortality_rate')) +
  scale_fill_gradient(low = 'deepskyblue', high = 'darksalmon') +
  xlab('Income Group') +
  ylab('Country') +
  labs(fill = 'Under-5 Mortality Rate') +
  ggtitle('Heatmap of Under-5 Mortality Rates\nby Income Group in Oceania') +
  theme(figure_size = (8.5,6))
)

