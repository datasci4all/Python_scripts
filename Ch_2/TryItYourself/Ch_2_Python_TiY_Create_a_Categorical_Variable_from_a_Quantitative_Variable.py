#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Create a Categorical Variable from a Quantitative Variable ####

# Importing necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('vote.csv')

# Categorize GPA
data["gpa_cat"] = np.where(data["gpa"] <= 2.99, "low", np.where(data["gpa"] >= 3.00,"high",np.NaN))


# Count the number of students in each GPA category
print("GPA counts:")
gpa_counts = data['gpa_cat'].value_counts()
print(gpa_counts)

