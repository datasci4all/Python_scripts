#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Calculate Similarity Using Distance ####

# Importing necessary libraries
import pandas as pd
from plotnine import ggplot, aes, geom_point, xlab, ylab, ggtitle, geom_text
from scipy.spatial import distance_matrix

# Import data
penguins = pd.read_csv('small_penguins.csv')

# Plot data
(ggplot(penguins, aes(x = "bill_length_mm", y = "bill_depth_mm", label='species')) +
  geom_point(size = 4) +
  xlab("Bill Length (mm)") +
  ylab("Bill Depth (mm)") +
  ggtitle("Bill Depth vs. Bill Length") +
  geom_text(nudge_y = 0.3)
)


# In[ ]:


penguin_bills = penguins[['bill_length_mm' , 'bill_depth_mm']]

# Compute distances
dist_matrix = pd.DataFrame(distance_matrix(penguin_bills, penguin_bills))
dist_matrix


# In[ ]:


# View original data set to see species
penguins


# In[ ]:


# Compute Min and Max Distances for Question 2
dist_mat = dist_matrix.to_numpy()

# Cluster 1
dist_mat1 = dist_mat[0:5, 0:5]
max_dist1 = max(dist_mat1.flatten())
print("Maximum distance between two points in Cluster 1: ", max_dist1, "\n")

dist_mat12 = dist_mat[0:5, 5:15]
min_dist1 = min(dist_mat12.flatten())
print("Distance from Cluster 1 to nearest other cluster using single linkage: ", min_dist1, "\n")

# Cluster 2
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
sliced_list = my_list[0:5] + my_list[10:15]

dist_mat2 = dist_mat[5:10, 5:10]
max_dist2 = max(dist_mat2.flatten())
print("Maximum distance between two points in Cluster 2: ", max_dist2, "\n")

dist_mat22 = dist_mat[5:10, sliced_list]
min_dist2 = min(dist_mat22.flatten())
print("Distance from Cluster 2 to nearest other cluster using single linkage: ", min_dist2, "\n")

# Cluster 3
dist_mat3 = dist_mat[10:15, 10:15]
max_dist3 = max(dist_mat3.flatten())
print("Maximum distance between two points in Cluster 3: ", max_dist3, "\n")

dist_mat32 = dist_mat[10:15, 0:10]
min_dist3 = min(dist_mat32.flatten())
print("Distance from Cluster 3 to nearest other cluster using single linkage: ", min_dist3, "\n")

