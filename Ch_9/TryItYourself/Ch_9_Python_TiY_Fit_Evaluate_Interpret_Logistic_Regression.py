#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Fit, Evaluate, and Interpret Logistic Regression ####

# Importing necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

# Import data
data_train = pd.read_csv('carseats_train.csv')
data_train = data_train.dropna()
data_test = pd.read_csv('carseats_test.csv')
data_test = data_test.dropna()

# Convert response variable to categorical variable
y_train = data_train['sales_cat'].astype('category').cat.rename_categories({'Low': 0, 'High': 1})
y_test = data_test['sales_cat'].astype('category').cat.rename_categories({'Low': 0, 'High': 1})


## Logistic Regression (1)
x_train = pd.DataFrame(data_train['advertising'])
x_test = pd.DataFrame(data_test['advertising'])

regression_pipeline = Pipeline(
  [('lr', LogisticRegression())]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_test)
accuracy_1 = accuracy_score(y_test, y_predicted)

print('Accuracy for Model 1:')
print(accuracy_1)


# In[ ]:


## Logistic Regression (2)
x_train = data_train[['advertising', 'population']]
x_test = data_test[['advertising', 'population']]

regression_pipeline = Pipeline(
  [('lr', LogisticRegression())]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_test)
accuracy_2 = accuracy_score(y_test, y_predicted)

print('Accuracy for Model 2:')
print(accuracy_2)


# In[ ]:


## Logistic Regression (3)
x_train = data_train[['advertising', 'population', 'shelf_location']]
x_test = data_test[['advertising', 'population', 'shelf_location']]

column_transformer = ColumnTransformer(
  [
    ('dummify', OneHotEncoder(sparse_output = False), ['shelf_location']),
  ],
  remainder = 'passthrough'
)

regression_pipeline = Pipeline(
  [('preprocessing', column_transformer),
   ('lr', LogisticRegression())]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_test)
accuracy_3 = accuracy_score(y_test, y_predicted)

print('Accuracy for Model 3:')
print(accuracy_3)


# In[ ]:


## Logistic Regression (4)
x_train = data_train[['advertising', 'population', 'shelf_location', 'age']]
x_test = data_test[['advertising', 'population', 'shelf_location', 'age']]

regression_pipeline = Pipeline(
  [('preprocessing', column_transformer),
   ('lr', LogisticRegression())]
).set_output(transform='pandas')

regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict(x_test)
accuracy_4 = accuracy_score(y_test, y_predicted)

print('Accuracy for Model 4:')
print(accuracy_4)
print('Coefficients of Model 4:')
coefs = pd.DataFrame.from_dict({'Term': column_transformer.transform(x_train).columns, 'Coefficient': regression_fitted['lr'].coef_[0]})
print(coefs)


# In[ ]:


# Predictions for two shelves

# Create a data frame for the new observations
new_store = {'age': [32, 60],
            'advertising': [6.3, 6.3],
            'shelf_location': ['Good', 'Good'],
            'population': [245.78, 245.78]
            }
new_store = pd.DataFrame(data = new_store)

# Fit logistic regression model
regression_pipeline = Pipeline(
  [('preprocessing', column_transformer),
    ('lr', LogisticRegression())]
).set_output(transform='pandas')


regression_fitted = regression_pipeline.fit(x_train, y_train)

y_predicted = regression_fitted.predict_proba(new_store)

# Print predictions
print('Probability Predictions for Two Stores:')
print('Low Sales at Store 1:', y_predicted[0, 0])
print('High Sales at Store 1:', y_predicted[0, 1])
print('Low Sales at Store 2:', y_predicted[1, 0])
print('High Sales at Store 2:', y_predicted[1, 1])

