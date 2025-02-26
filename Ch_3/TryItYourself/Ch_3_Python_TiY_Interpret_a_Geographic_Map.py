#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Geographic Map ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, xlab, ylab, geom_polygon, scale_fill_gradient, labs, theme_bw, geom_text, ggtitle

# Import the data
countries = pd.read_csv('countries.csv')

south_america = countries[countries['continent'] == 'South America'].rename(columns={'country': 'region'})

world = pd.read_csv('world_map_data.csv')

combined_data = world.merge(south_america, on = 'region', how = 'left')
country_labels = combined_data.groupby('region')[['long', 'lat', 'group']].mean().reset_index()

# Plot the data
(ggplot(combined_data, aes(x = 'long', y = 'lat', group = 'group')) +
  geom_polygon(aes(fill = 'gni_per_capita'), color = 'white', size = 0.2) +
  scale_fill_gradient(low='#D35FB7', high='#FEFE62', limits = [4000, 27500]) +
  theme_bw() +
  geom_text(country_labels, aes(x = 'long', y = 'lat', label = 'region', group = 'group'), size = 4) +
  xlab('') +
  ylab('') +
  labs(fill = 'GNI per Capita') +
  ggtitle('Map of GNI per Capita in South America by Country')
)

