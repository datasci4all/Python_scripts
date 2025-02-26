#!/usr/bin/env python
# coding: utf-8

# In[3]:


#### Interpretability vs. Complexity ####

# Importing necessary libraries
import pandas as pd
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv('carseats.csv')

# Model piece to handle categorical variables
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['shelf_location', 'urban', 'us']),
  ],
  remainder = 'passthrough'
)

x_train = data.drop(['sales', 'sales_cat'], axis=1)
y_train = data['sales_cat'].astype('category').cat.codes


## Classification Tree (Max Depth = 1)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeClassifier(max_depth=1))]
).set_output(transform='pandas')

# Fit and plot tree
tree_fitted = tree_pipeline.fit(x_train, y_train)
tree.plot_tree(tree_fitted['tree'], feature_names = list(column_transformer.transform(X_train).columns),
                filled = True, class_names = sorted(list(data['sales_cat'].unique())), impurity = False
    )


# In[4]:


## Classification Tree (Max Depth = 5)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10))]
).set_output(transform='pandas')

# Fit and plot tree
tree_fitted = tree_pipeline.fit(X_train, y_train)

plt.figure(figsize=(12,6)) #adjust width and height of the figure to make your tree readable
tree.plot_tree(tree_fitted['tree'], feature_names = list(column_transformer.transform(X_train).columns),
                filled = True, class_names = sorted(list(data['sales_cat'].unique())), impurity = False, fontsize = 8
    )


# In[5]:


## Classification Tree (Max Depth = 20)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeClassifier(max_depth=20, max_leaf_nodes=20))]
).set_output(transform='pandas')

# Fit and plot tree
tree_fitted = tree_pipeline.fit(X_train, y_train)

plt.figure(figsize=(15,10)) #adjust width and height of the figure to make your tree readable
tree.plot_tree(tree_fitted['tree'], feature_names = list(column_transformer.transform(X_train).columns),
                filled = True, class_names = sorted(list(data['sales_cat'].unique())), impurity = False, fontsize = 8
    )

