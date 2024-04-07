# Importing the required packages
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
import joblib
from sklearn.impute import SimpleImputer

# Import and seperate the dataset into two categories: categorical_columns and numeric_columns  
dataset = pd.read_csv('train.csv')
categorical_columns = dataset.select_dtypes(include=['object']).columns.tolist()
numeric_columns = dataset.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Remove unwanted Columns
columns_2_remove = ['Loan_ID', 'Loan_Status']
categorical_columns = [cols for cols in categorical_columns if cols not in columns_2_remove]


# Filling nulls in the dataset
categorical_imputer = SimpleImputer(strategy='most_frequent')
numeric_imputer = SimpleImputer(strategy='median')
dataset[categorical_columns] = categorical_imputer.fit_transform(dataset[categorical_columns])
dataset[numeric_columns] = numeric_imputer.fit_transform(dataset[numeric_columns])

# Dealing with outliers
columns_2_transform = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
for col in columns_2_transform:
    dataset[col] = np.log1p(dataset[col])

# Data Processing
dataset['TotalIncome'] = dataset['ApplicantIncome'] + dataset['CoapplicantIncome']
columns_2_drop = ['ApplicantIncome', 'CoapplicantIncome']
dataset = dataset.drop(columns = columns_2_drop)

le = LabelEncoder()
for col in categorical_columns:
    dataset[col] = le.fit_transform(dataset[col])

dataset['Loan_Status'] = le.fit_transform(dataset['Loan_Status'])

# DataSplit and Model Fit
X = dataset.drop(columns = ['Loan_Status', 'Loan_ID'])
y = dataset['Loan_Status']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

# RandomForest
rf = RandomForestClassifier(random_state=42)
model_forest = rf.fit(X, y)

joblib.dump(model_forest, 'RF_Loan_model.pkl')

print("Welcome to Loan Prediction Application")
print("Enter your details to get to know the application status as per the instruction below:")
print("Type 'exit' to terminate.....\n")
print('''Gender: Female = 0, Male=1
Married: No = 0, Yes = 1
Education: Graduate = 0 , Under-graduate = 1
Self_Employed: No = 0, Yes = 1
Property_Area: Urban = 2, Semiurban = 1, Rural = 0
Loan_Status: No = 0, Yes = 1\n''')

print('''Enter the data with the below mentioned order , where values are seperated by comma: 
Gender, Married, Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,TotalIncome\n''')

while True:
    user_data=input("Enter your Details: ")
    
    if(user_data=="exit"):
        break

    data = list(map(float, user_data.split(','))) # convert to float

    # basic validation
    if(len(data)<10):
        print("Incomplete data provided!!")
    else:
        
        # predicting the value
        predicted_value=model_forest.predict([data])
        print("/**********************************************************************/")
        if (predicted_value[0]):
            print("\tCongratulations! your loan request is Approved")
        else:
            print("\tSorry! your loan request is Rejected, please try again after 6 months")
        print("/**********************************************************************/")