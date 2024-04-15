# main.py file
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import pandas as pd 
import numpy as np
from typing import List, Dict

# CORSMiddleware: Cross-Origin-Resource-Sharing-MiddleWare
from fastapi.middleware.cors import CORSMiddleware
from MLPackages.predict import generate_predictions

app = FastAPI(
    title="Loan-Prediction APP using FastAPI + CICD Jenkins",
    description="A small Demo on CICD",
    version='1.0'
)

# https://www.youtube.com/watch?v=4KHiSt0oLJ0&ab_channel=Fireship
# Meaning, we're allowing everything
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=['*'],
    allow_headers=['*'])

class LoanPrediction(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str
    
@app.get("/")
def index():
    return {"message":"Welcome to Loan Prediction App using API - CI CD Jenkins" }

@app.post("/prediction_api")
def predict(loan_details: LoanPrediction):
    data = loan_details.model_dump()
    prediction = generate_predictions([data])["prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status":pred}

@app.post("/prediction_ui")
def predict_gui(gender: str,
    married: str,
    dependents: str,
    education: str,
    self_employed: str,
    applicant_income: float,
    coapplicant_income: float,
    loan_amount: float,
    loan_amount_term: float,
    credit_history: float,
    property_area: str):


    input_data = [gender, married, dependents, education, self_employed, applicant_income,
     coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]
    
    cols = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    
    data_dict = dict(zip(cols,input_data))
    prediction = generate_predictions([data_dict])["prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status":pred}

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)