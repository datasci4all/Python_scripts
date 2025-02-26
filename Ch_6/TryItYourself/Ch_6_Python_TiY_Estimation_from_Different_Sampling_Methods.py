#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Estimation from Different Sampling Methods ####

# Importing necessary libraries
import pandas as pd

## SRS Stats
print('SRS Statistics:')
srs = pd.read_csv('student_socialmedia_srs.csv')

print(srs.groupby('class').agg(['mean', 'count']))

print('Overall average:')
print(srs['social_media'].mean())

## Proportional Stratified Stats
print('Stratified Random Sample Statistics:')
strat_samp = pd.read_csv('student_socialmedia_strat.csv')

print(strat_samp.groupby('class').agg(['mean', 'count']))

print('Overall average:')
print(strat_samp['social_media'].mean())


## Balanced Stratified Stats
print('Balanced Stratified Random Sample Statistics:')
bal_strat_samp = pd.read_csv('student_socialmedia_bal_strat.csv')

print(bal_strat_samp.groupby('class').agg(['mean', 'count']))

print('Overall average:')
print(bal_strat_samp['social_media'].mean())

