#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing necessary libraries
import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset
data = pd.read_csv('pizzapasta.csv')  # Replace with the actual file path

# Separate the data into two groups based on the image seen
pizza_group = data[data['treatment'] == 'pizza']
pasta_group = data[data['treatment'] == 'pasta']

# Calculate the number of participants in each group
num_pizza_participants = pizza_group.shape[0]
num_pasta_participants = pasta_group.shape[0]

# Calculate the mean session duration for each group
mean_session_pizza = pizza_group['session_duration'].mean()
mean_session_pasta = pasta_group['session_duration'].mean()

# Perform t-tests for session duration and purchase portion
t_stat_session, p_value_session = ttest_ind(pizza_group['session_duration'], pasta_group['session_duration'], equal_var=True, alternative = 'greater')


# Output the results
print('Number of Participants - Pizza Image:', num_pizza_participants)
print('Number of Participants - Pasta Image:', num_pasta_participants)
print('Mean Session Duration - Pizza Image:', mean_session_pizza)
print('Mean Session Duration - Pasta Image:', mean_session_pasta)
print('P-Value for Session Duration:', p_value_session)


