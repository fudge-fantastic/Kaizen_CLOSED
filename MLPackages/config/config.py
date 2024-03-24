import os
import sys
path1 = os.getcwd()
path2 = os.path.dirname(path1)
path3 = os.path.dirname(path2)
sys.path.append(path3)

# Pathlib is used to interact with the file system in our Python programs
import pathlib
import MLPackages

# This helps me to locate the package files
ROOT_PACKAGES = pathlib.Path(MLPackages.__file__).resolve().parent

# Path to the datasets
DATAPATH = os.path.join(ROOT_PACKAGES, "datasets")
TRAIN_DATA = "train.csv"
TEST_DATA = "test.csv"

# Trained and Saved models
npath1 = os.path.dirname(MLPackages.__file__)
MODEL_SAVED = "classification_model.pkl"
SAVED_MODEL_PATH = os.path.join(npath1, 'trained_models')
# SAVED_MODEL_PATH = os.path.join(ROOT_PACKAGES, "trained_models")

TARGET = ['Loan_Status']

FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
       'Property_Area', 'CoapplicantIncome']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'Credit_History', 'Property_Area']

FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'Credit_History', 'Property_Area']

# Recall the time, when we added a new feature in our ipynb file
FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'

FEATURE_TO_DROP = ['CoapplicantIncome']

FEATURES_TO_TRANSFORM = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']


# def if_working():
#     word = print("Working well without import errors")
#     return word

# if __name__ == '__main__':
#     if_working()