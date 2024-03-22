# Pathlib is used to interact with the file system in our Python programs
import pathlib
import os
import MLPackages

# This helps me to locate the package files
ROOT_PACKAGES = pathlib.Path(MLPackages.__file__).resolve().parent

# Path to the datasets
DATAPATH = os.path.join(ROOT_PACKAGES, "datasets")
TRAIN_DATA = "train.csv"
TEST_DATA = "test.csv"

# Trained and Saved models
MODEL_SAVED = "classification.pkl"
SAVED_MODEL_PATH = os.path.join(ROOT_PACKAGES, "trained_models")

TARGET = ['Loan_Status']

FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
       'Property_Area', 'CoApplicantIncome']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'Credit_History', 'Property_Area']

FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'Credit_History', 'Property_Area']

# Recall the time, when we added a new feature in our ipynb file
FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoApplicantIncome'

FEATURE_TO_DROP = ['CoApplicantIncome']

FEATURES_TO_TRANSFORM = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']