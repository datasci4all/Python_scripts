#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Compare Cluster Analysis Results ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, xlab, ylab, ggtitle, scale_x_continuous, scale_y_continuous, labs
from sklearn.cluster import KMeans

# Import data
data = pd.read_csv('small_music.csv')

# Plot data without clustering
(ggplot(data, aes(x = 'danceability', y = 'energy')) +
  geom_point(size = 3) +
  ylab('Energy') +
  xlab('Danceability') +
  ggtitle('Energy vs. Danceability')
)


# In[ ]:


## 2 cluster analysis
data_variables = data[['danceability', 'energy']]
k_means_clustering = KMeans(n_clusters = 2, random_state = 1, algorithm = 'lloyd').fit(data_variables)

data['clusters2'] = [str(x) for x in k_means_clustering.labels_]

# Plot results from 2 cluster analysis
(ggplot(data, aes(x = 'danceability', y = 'energy')) +
  geom_point(aes(fill = 'clusters2'), color = 'black', size = 3) +
  ylab('Energy') +
  xlab('Danceability') +
  labs(fill = 'Cluster') +
  ggtitle('Energy vs. Danceability')
)


# In[ ]:


## 4 cluster analysis
k_means_clustering = KMeans(n_clusters = 4, random_state = 1, algorithm = 'lloyd').fit(data_variables)

data['clusters4'] = [str(x) for x in k_means_clustering.labels_]

# Plot 4 cluster analysis
(ggplot(data, aes(x = 'danceability', y = 'energy')) +
  geom_point(aes(fill = 'clusters4'), color = 'black', size = 3) +
  ylab('Energy') +
  xlab('Danceability') +
  labs(fill = 'Cluster') +
  ggtitle('Energy vs. Danceability')
)


# In[ ]:


## 6 cluster analysis
k_means_clustering = KMeans(n_clusters = 6, random_state = 1, algorithm = 'lloyd').fit(data_variables)

data['clusters6'] = [str(x) for x in k_means_clustering.labels_]

# Plot 6 cluster analysis
(ggplot(data, aes(x = 'danceability', y = 'energy')) +
  geom_point(aes(fill = 'clusters6'), color = 'black', size = 3) +
  ylab('Energy') +
  xlab('Danceability') +
  labs(fill = 'Cluster') +
  ggtitle('Energy vs. Danceability')
)

