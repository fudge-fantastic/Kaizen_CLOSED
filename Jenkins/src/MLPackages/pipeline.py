import os
import sys

path1 = os.getcwd()
path2 = os.path.dirname(path1)
sys.path.append(path2)

from sklearn.pipeline import Pipeline
from MLPackages.config import config
from MLPackages.processing import preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np
import MLPackages

path3 = os.path.dirname(MLPackages.__file__)
path4 = os.path.join(path3, 'classification.pkl')

saved_model = joblib.load(path4)

classification_pipeline = Pipeline(
    [
        ('MeanImputation', pp.MeanImputer(variables=config.NUM_FEATURES)),
        ('ModeImputation', pp.ModeImputer(variables=config.CAT_FEATURES)),
        ('DomainProcessing', pp.DomainProcessing(variables_to_modify=config.FEATURE_TO_MODIFY, variables_to_add=config.FEATURE_TO_ADD)),
        ('DropColumns', pp.DropColumns(variables_to_drop=config.FEATURE_TO_DROP)),
        ('LabelEncoder', pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
        ('LogTransformation', pp.LogTransformer(variables=config.FEATURES_TO_TRANSFORM)),
        # Here you CAN create your custom Scaler, but we'll use the default Scaler
        ('MinMaxScaler', MinMaxScaler()),
        ('Model', saved_model)
    ]
)

# def if_working():
#     word = print("Working well without import errors")
#     return word

# if __name__ == '__main__':
#     if_working()