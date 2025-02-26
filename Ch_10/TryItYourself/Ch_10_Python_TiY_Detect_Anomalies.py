#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import numpy as np
import pandas as pd

# eBay winning bids for a new bird cage in US dollars
bids = np.array([88, 92, 95, 76, 89, 40, 180, 15, 90, 80, 85, 91, 20])

# Calculating the mean and standard deviation
mean = bids.mean()
std_dev = bids.std(ddof=1)

# Calculating Z-scores (standardized scores)
z_scores = (bids - mean) / std_dev

# Combining bids and scores
formatted_z_scores = pd.DataFrame({
    'bids': bids,
    'scores': z_scores
})
print(formatted_z_scores)

print('Mean:', mean)
print('Standard Deviation:', std_dev)

