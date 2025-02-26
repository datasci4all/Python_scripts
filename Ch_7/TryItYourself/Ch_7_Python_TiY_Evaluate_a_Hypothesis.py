#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
import random
import numpy as np
from plotnine import ggplot, aes, geom_histogram, ggtitle, labs, geom_vline

# Load the data from the CSV file
school_data = pd.read_csv('school.csv')

# Filtering the data to include only classes with an average difficulty rating of at least 3
difficult_classes = school_data[school_data['avg_course_difficulty'] >= 3]

# Calculating the proportion of students in difficult classes
proportion_difficult_classes = len(difficult_classes) / len(school_data)

print('The proportion of students from our sample in classes with an average difficulty rating of at least 3:')
print(proportion_difficult_classes)


# In[ ]:


# Perform the simulation-based hypothesis test

# Create dataframe to hold simulation results
num_students = len(school_data) # Numbers of Flips
num_sim = 10000
data_sim = pd.DataFrame({
  'proportion_sim' : [0.0]*num_sim,
})

null_value = 0.65

# Perform simulation
for i in np.arange(num_sim):
    sim = random.choices([1, 0], weights = [null_value, 1-null_value], k = num_students)

    data_sim.loc[i, 'proportion_sim'] = sum(np.equal(sim, 1))/num_students

# Plot the simulation results
(ggplot(data_sim, aes(x = 'proportion_sim')) +
  geom_histogram(alpha = .55, bins = 20, boundary = proportion_difficult_classes) +
  geom_vline(xintercept = proportion_difficult_classes, color = 'red') +
  labs(
      x = 'Sample Proportion of Students Attending Difficult Courses',
      y = 'Count'
  ) +
  ggtitle('Distribution of Sample Proportions')
)


# In[ ]:


# Compute and print the p-value
print('P-value:')
print(sum(data_sim['proportion_sim'] > proportion_difficult_classes)/num_sim)

