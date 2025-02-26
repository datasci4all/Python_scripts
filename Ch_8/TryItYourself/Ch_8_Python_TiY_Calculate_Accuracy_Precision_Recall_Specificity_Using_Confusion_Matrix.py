#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Calculate Accuracy, Precision, Recall, and Specificity using a Confusion Matrix ####

# Importing necessary libraries
import pandas as pd
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Import data
data_train = pd.read_csv('carseats_train.csv')
data_test = pd.read_csv('carseats_test.csv')

# Model piece to handle categorical variables
column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['shelf_location', 'urban', 'us']),
  ],
  remainder = 'passthrough'
)

# Distinguish training and test data
x_train = data_train.drop(['sales', 'sales_cat'], axis=1)
y_train = data_train['sales_cat'].astype('category').cat.codes
x_test = data_test.drop(['sales', 'sales_cat'], axis=1)
y_test = data_test['sales_cat'].astype('category').cat.codes


## Classification Tree (Max Depth = 5)
tree_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('tree', DecisionTreeClassifier(max_depth=5, min_samples_split=2, ccp_alpha=0, random_state=1234))]
).set_output(transform='pandas')

# Fit tree
tree_fitted = tree_pipeline.fit(x_train, y_train)

# Compute predictions
y_predicted = tree_pipeline.predict(x_test)

# Print confusion matrix
print('Confusion matrix for test data:')
confusion_matrix = confusion_matrix(y_test, y_predicted)
print(confusion_matrix)

print('Accuracy:')
print((confusion_matrix[0,0] + confusion_matrix[1,1])/len(y_test))

print('Precision:')
print(confusion_matrix[0,0]/(confusion_matrix[0,0] + confusion_matrix[0,1]))

print('Recall:')
print(confusion_matrix[0,0]/(confusion_matrix[0,0] + confusion_matrix[1,0]))

print('Specificity:')
print(confusion_matrix[1,1]/(confusion_matrix[1,1] + confusion_matrix[1,0]))

