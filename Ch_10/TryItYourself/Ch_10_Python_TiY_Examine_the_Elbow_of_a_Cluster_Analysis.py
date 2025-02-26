#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Examine the Elbow of a Cluster Analysis ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_line, xlab, ylab, ggtitle, labs, geom_point
from sklearn.cluster import KMeans

# Import data
data = pd.read_csv('penguins.csv')

# Scale data
data['body_mass_g'] = (data['body_mass_g'] - data['body_mass_g'].mean())/data['body_mass_g'].std()
data['bill_length_mm'] = (data['bill_length_mm'] - data['bill_length_mm'].mean())/data['bill_length_mm'].std()
data['bill_depth_mm'] = (data['bill_depth_mm'] - data['bill_depth_mm'].mean())/data['bill_depth_mm'].std()
data['flipper_length_mm'] = (data['flipper_length_mm'] - data['flipper_length_mm'].mean())/data['flipper_length_mm'].std()

k_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
inertia = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# k-means cluster analysis for different k
for i in range(len(k_values)):
    k_means_clustering = KMeans(n_clusters = k_values[i], random_state = 100,
              algorithm = 'lloyd').fit(data[['bill_length_mm', 'bill_depth_mm',
                                            'flipper_length_mm', 'body_mass_g']])

    inertia[i] = k_means_clustering.inertia_

# Organize information into a dataframe
data_result = pd.DataFrame({'k_values': k_values})
data_result['inertia'] = inertia

# Plot k-means cluster analysis results
(ggplot(data_result, aes(x = 'k_values', y = 'inertia')) +
  geom_point(size = 2) +
  geom_line() +
  xlab('Number of Clusters (k)') +
  ylab('Within-Cluster Variability (Inertia)') +
  ggtitle('Within-Cluster Variability vs. Number of Clusters')
)

