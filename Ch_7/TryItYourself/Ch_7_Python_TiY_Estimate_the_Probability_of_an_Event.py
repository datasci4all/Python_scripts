#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_histogram, labs

# Setting the seed for reproducibility
np.random.seed(777)

# Coin-Flipping Simulation
nullp = 0.5
num_flips = 100

# Null Distribution Simulation with 100
num_sims = 100
null_flips = [np.sum(np.random.choice([1, 0], size=num_flips, p=[nullp, 1-nullp])) for _ in range(num_sims)]
null_data = pd.DataFrame({'num_heads': null_flips})


# In[ ]:


# Compute number of times 60 heads came up
print('Number of times 60 heads came up:')
print(sum(null_data['num_heads'] == 60))


# In[ ]:


# Compute probability of times 60 heads coming up
print('Probability of times 60 heads coming up:')
print(sum(null_data['num_heads'] == 60)/100)

