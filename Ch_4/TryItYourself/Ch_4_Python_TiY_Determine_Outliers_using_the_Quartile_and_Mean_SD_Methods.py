#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Determine Outliers using the Quartile and Mean/SD Methods ####

# Importing necessary libraries
import pandas as pd

# Load the dataset
videogames_df = pd.read_csv('videogames.csv')

# Calculating the mean, standard deviation, quartiles and IQR for 'global_sales'
mean_global_sales = videogames_df['global_sales'].mean()
std_global_sales = videogames_df['global_sales'].std()
q1 = videogames_df['global_sales'].quantile(0.25)
q3 = videogames_df['global_sales'].quantile(0.75)
iqr = q3 - q1

# Quartile Method Thresholds
mild_outliers_q_low = q1 - 1.5 * iqr
mild_outliers_q_high = q3 + 1.5 * iqr
regular_outliers_q_low = q1 - 3 * iqr
regular_outliers_q_high = q3 + 3 * iqr

# Mean/SD Method Thresholds
mild_outliers_sd_low = mean_global_sales - 2 * std_global_sales
mild_outliers_sd_high = mean_global_sales + 2 * std_global_sales
regular_outliers_sd_low = mean_global_sales - 3 * std_global_sales
regular_outliers_sd_high = mean_global_sales + 3 * std_global_sales

# Creating a table to display the results
outlier_thresholds = pd.DataFrame({
    'Type': ['Mild Outliers', 'Regular Outliers', 'Mild Outliers', 'Regular Outliers'],
    'Method': ['Quartile Method', 'Quartile Method', 'Mean/SD Method', 'Mean/SD Method'],
    'Lower Threshold': [mild_outliers_q_low, regular_outliers_q_low, mild_outliers_sd_low, regular_outliers_sd_low],
    'Upper Threshold': [mild_outliers_q_high, regular_outliers_q_high, mild_outliers_sd_high, regular_outliers_sd_high]
})

print(outlier_thresholds)

outlier_count = {
    'Mild Outliers (Quartile Method)': (videogames_df['global_sales'] > mild_outliers_q_high).sum(),
    'Regular Outliers (Quartile Method)': (videogames_df['global_sales'] > regular_outliers_q_high).sum(),
    'Mild Outliers (Mean/SD Method)': (videogames_df['global_sales'] > mild_outliers_sd_high).sum(),
    'Regular Outliers (Mean/SD Method)': (videogames_df['global_sales'] > regular_outliers_sd_high).sum()
}

# Print the count of outliers
print(outlier_count)


