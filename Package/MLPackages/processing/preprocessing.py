import os
import sys
path1 = os.getcwd()
path2 = os.path.dirname(path1)
path3 = os.path.dirname(path2)
sys.path.append(path3)

from sklearn.base import BaseEstimator, TransformerMixin
from MLPackages.config import config
import numpy as np


# Mean Imputer for numeric columns
class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables = None):
        self.variables = variables
        
    def fit(self, X, y= None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mean_dict[col], inplace = True)
        return X 
    
# Mode Imputer for categorical columns
class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables = None):
        self.variables = variables
        
    def fit(self, X, y= None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mode_dict[col], inplace = True)
        return X
    
    
# Class to drop the columns
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X = X.drop(columns=self.variables_to_drop)
        return X
    
# This can be any function, according to the domain
class DomainProcessing(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_modify=None, variables_to_add=None):
        self.variables_to_modify = variables_to_modify
        self.variables_to_add = variables_to_add
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for features in self.variables_to_modify:
            X[features] = X[features] + X[self.variables_to_add]
        return X
    
# Label Encoder
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables
        
    def fit(self, X, y):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index
            self.label_dict[var] = {k: i for i, k in enumerate(t, 0)}
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X
    

class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, variables = None):
        self.variables = variables
        
    def fit(self, X, y= None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = np.log(X[col])
        return X
   

# def if_working():
#     word = print("Working well without import errors")
#     return word

# if __name__ == '__main__':
#     if_working()