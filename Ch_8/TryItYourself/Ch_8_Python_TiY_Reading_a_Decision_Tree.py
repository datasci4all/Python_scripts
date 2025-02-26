#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Reading a Decision Tree ####

# Importing necessary libraries
import pandas as pd
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Import data
penguins = pd.read_csv('penguins.csv')

# Model piece to handle categorical variables
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['island', 'sex']),
  ],
  remainder = 'passthrough'
)

# Build decision tree model
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeClassifier(max_depth=1))]
).set_output(transform='pandas')

# Fit and plot tree
x_train = penguins.drop('species', axis=1)
y_train = penguins['species'].astype('category').cat.codes
tree_fitted = tree_pipeline.fit(x_train, y_train)
tree.plot_tree(tree_fitted['tree'], feature_names = list(column_transformer.transform(x_train).columns),
                filled = True, class_names = sorted(list(penguins['species'].unique())), impurity = False
    )

