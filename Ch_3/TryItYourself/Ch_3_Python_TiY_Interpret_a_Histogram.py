#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Interpret a Histogram ####
# Import necessary libraries
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_histogram, xlab, ggtitle, theme_minimal

# Import data
countries = pd.read_csv('countries.csv')

# Calculate bin edges manually to match Excel
min_gni = countries['gni_per_capita'].min()
max_gni = countries['gni_per_capita'].max()

# Create 20 bins (you can adjust the number if needed)
bins = np.linspace(min_gni, max_gni, 21)  # 21 edges for 20 bins

# Plot using plotnine with manual binning
plot = (ggplot(countries, aes(x='gni_per_capita')) +
        geom_histogram(breaks=bins, fill='#0072b2', color='black') +  # Manually set bin breaks
        xlab('GNI Per Capita ($)') +
        ggtitle('Gross National Income Per Capita Worldwide')
       )

# Display the plot
print(plot)

