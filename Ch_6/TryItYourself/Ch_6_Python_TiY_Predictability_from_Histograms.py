#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Predictability from Histograms ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_histogram, facet_wrap, labs

# Import data
pinball = pd.read_csv('pinball.csv')

# Plot data
(ggplot(pinball, aes(x = 'scores', fill = 'person')) +
  geom_histogram() +
  facet_wrap('person', nrow = 3) +
  labs(
    fill = 'Gamer',
    x = 'Pinball Scores (in millions)'
  )
)


# In[ ]:


# Compute averages
print('Average Pinball Scores:')
print(pinball.groupby('person').mean())

# Compute proportions
print('Proportion of Darc's Scores Over 1250 million:')
print(sum(pinball['scores'][pinball['person'] == 'Darc'] > 1250)/1000)
print('Proportion of Qpawnz's Scores Over 1250 million:')
print(sum(pinball['scores'][pinball['person'] == 'Qpawnz'] > 1250)/1000)
print('Proportion of Ember's Scores Over 1250 million:')
print(sum(pinball['scores'][pinball['person'] == 'Ember'] > 1250)/1000)

