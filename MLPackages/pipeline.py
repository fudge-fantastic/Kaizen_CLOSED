from sklearn.pipeline import Pipeline
from MLPackages.config import config
from MLPackages.processing import preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np

saved_model = joblib.load('trained_model_loan_exp_LR.pkl')

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
