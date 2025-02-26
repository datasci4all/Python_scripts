#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
import random
import numpy as np
from plotnine import ggplot, aes, geom_histogram, ggtitle, labs, geom_vline
from scipy.stats import pearsonr

# Load the dataset
data = pd.read_csv('school.csv')

# Extracting GPA and AvgCourseDifficulty
gpa = data['gpa']
course_difficulty = data['avg_course_difficulty']

# Calculating the Pearson correlation coefficient and p-value
correlation_coefficient, correlation_p = pearsonr(gpa, course_difficulty)

# Output the results
print('Observed correlation coefficient:')
print(correlation_coefficient)


# In[ ]:


# Peform simulation-based hypothesis test

# Create dataframe to store simulations in
num_sim = 10000
data_sim = pd.DataFrame({
  'correlation' : [0.0]*num_sim,
})

null_value = 0

# Perform simulations
for i in np.arange(num_sim):
    correlation_sim, correlation_p = pearsonr(course_difficulty, random.sample(sorted(gpa), k = len(gpa)))

    data_sim.loc[i, 'correlation'] = correlation_sim

# Plot simulations
(ggplot(data_sim, aes(x = 'correlation')) +
  geom_histogram(alpha = .55, bins = 20, boundary = correlation_coefficient) +
  geom_vline(xintercept = correlation_coefficient, color = 'red') +
  labs(
      x = 'Sample Correlation',
      y = 'Count'
  ) +
  ggtitle('Distribution of Sample Correlations')
)


# In[ ]:


# Compute and print p-value
print('P-value:')
print(sum(data_sim['correlation'] < correlation_coefficient)/num_sim)

