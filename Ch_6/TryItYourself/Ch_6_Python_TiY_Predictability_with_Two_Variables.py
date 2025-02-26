#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Predictability with Two Variables ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, ylim, labs, ggtitle

# Import data
pinball = pd.read_csv('pinball_sleep_caffeine.csv')

# Plot scores vs. sleep
(ggplot(pinball, aes(x = 'sleep', y = 'scores')) +
  geom_point(size = 2.5) +
  ylim(0, 1500) +
  labs(
    x = 'Sleep (hours)',
    y = 'Pinball Score (in millions)'
  ) +
  ggtitle('Pinball Score vs. Sleep')
)


# In[ ]:


# Plot scores vs. caffeine
(ggplot(pinball, aes(x = 'caffeine', y = 'scores')) +
  geom_point(size = 2) +
  ylim(0, 1500) +
  labs(
    x = 'Caffeine (mg)',
    y = 'Pinball Score (in millions)'
  ) +
  ggtitle('Pinball Score vs. Caffeine Consumed')
)

