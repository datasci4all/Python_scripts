#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Simulate Samples ####
#### Fair Coin ####

# Importing necessary libraries
import pandas as pd
import random
import numpy as np
from plotnine import ggplot, aes, geom_histogram, facet_wrap, ylab, xlab, ggtitle, labs
random.seed(1234)

# Create data frame to hold results in
ns = [30, 100, 1000] # Numbers of Flips
sim_n = 10000
d = pd.DataFrame({
  'sample_size30' : [0]*sim_n,
  'sample_size100' : [0]*sim_n,
  'sample_size1000' : [0]*sim_n,
})

# Perform simulations
k = 0
for i in np.arange(sim_n):
    x = random.choices(['Heads', 'Tails'], k = ns[0])
    x2 = random.choices(['Heads', 'Tails'], k = ns[1])
    x3 = random.choices(['Heads', 'Tails'], k = ns[2])

    d['sample_size30'][k] = sum(np.char.equal(x, 'Heads'))/ns[0]
    d['sample_size100'][k] = sum(np.char.equal(x2, 'Heads'))/ns[1]
    d['sample_size1000'][k] = sum(np.char.equal(x3, 'Heads'))/ns[2]
    k = k + 1

# Organize results
d2 = d.melt(value_vars = ['sample_size30', 'sample_size100', 'sample_size1000'], var_name = 'sample_size', value_name = 'prop')
d2['n'] = ''
d2['n'][d2['sample_size'] == 'sample_size30'] = '30'
d2['n'][d2['sample_size'] == 'sample_size100'] = '100'
d2['n'][d2['sample_size'] == 'sample_size1000'] = '1000'

d2['n'] = d2['n'].astype('category').cat.reorder_categories(['1000', '100', '30'], ordered = True)

# Plot results
(ggplot(d2, aes(x = 'prop', fill = 'n')) +
  geom_histogram(alpha = .55, bins = 20) +
  facet_wrap('n', nrow = 3) +
  xlab('Sample Proportion of Heads') +
  ylab('Count') +
  labs(fill = 'Sample Size') +
  ggtitle('Distribution of Sample Proportion of Heads')
)

