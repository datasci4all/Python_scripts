#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Estimating Likelihood of Values in Data ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_histogram, ggtitle, xlab, ylab

# Import data
college = pd.read_csv('college.csv')

# Plot data
(ggplot(college, aes(x = 'f_undergrad')) +
  geom_histogram() +
  ggtitle('Number of Full-time Undergraduates') +
  ylab('Count') +
  xlab('Number of Full-time Undergraduates')
)


# In[ ]:


# Compute proportions
print('Proportion of schools with less than 5000 full-time undergraduates')
print(len(college['f_undergrad'][college['f_undergrad'] < 5000])/len(college))

print('Proportion of schools with more than 15000 full-time undergraduates')
print(len(college['f_undergrad'][college['f_undergrad'] > 15000])/len(college))

