#!/usr/bin/env python3

import os
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
import mlflow
from sklearn import metrics
import matplotlib.pyplot as plt 

# Function to read and preprocess data
def preprocess_data(filepath):
    # Import and separate the dataset into two categories: categorical_columns and numeric_columns  
    dataset = pd.read_csv(filepath)
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
    
    return dataset

# Function to split data
def split_data(dataset):
    X = dataset.drop(columns = ['Loan_Status', 'Loan_ID'])
    y = dataset['Loan_Status']
    return train_test_split(X, y, test_size=0.3, random_state=21)

# Function to train models
def train_models(X_train, y_train):
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'DecisionTreeClassifier': DecisionTreeClassifier(),
        'GradientBoostingClassifier': GradientBoostingClassifier(),
        'AdaBoostClassifier': AdaBoostClassifier(algorithm='SAMME')
    }
    trained_models = {name: model.fit(X_train, y_train) for name, model in models.items()}
    return trained_models

# Function to evaluate metrics
def eval_metrics(actual, pred):
    accuracy = metrics.accuracy_score(actual, pred)*100
    precision = metrics.precision_score(actual, pred)*100
    recall = metrics.recall_score(actual, pred)*100
    f1 = metrics.f1_score(actual, pred)*100
    fpr, tpr, _ = metrics.roc_curve(actual, pred)
    auc = metrics.auc(fpr, tpr)*100
    
    # Plot ROC curve
    plt.figure(figsize=(8,8))
    plt.plot(fpr, tpr, color='blue', label='ROC curve area = %0.2f' % auc)
    plt.plot([0,1], [0,1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend(loc='lower right')
    
    # Save plot
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/ROC_curve.png")
    plt.close()
    
    return (accuracy, precision, recall, f1, auc)

# Function to log metrics and models with MLflow
def mlflow_logging(model, X, y, name):
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        mlflow.set_tag("run_id", run_id)
        pred = model.predict(X)
        # Calculate evaluation metrics
        (accuracy, precision, recall, f1, auc) = eval_metrics(y, pred)
        # Log evaluation metrics
        mlflow.log_metric("Accuracy", accuracy)
        mlflow.log_metric("Precision", precision)
        mlflow.log_metric("Recall", recall)
        mlflow.log_metric("F1-score", f1)
        mlflow.log_metric("AUC", auc)
        # Log artifacts and model
        mlflow.log_artifact("plots/ROC_curve.png")
        mlflow.sklearn.log_model(model, name)

# Main function
def main():
    mlflow.set_tracking_uri("http://localhost:5000/")
    mlflow.set_experiment("Loan_Prediction")
    
    dataset = preprocess_data('train.csv')
    X_train, X_test, y_train, y_test = split_data(dataset)
    trained_models = train_models(X_train, y_train)
    
    for name, model in trained_models.items():
        mlflow_logging(model, X_test, y_test, name)

if __name__ == "__main__":
    main()
