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

    @classmethod
    def from_input_data(cls, input_data: List[str]) -> 'LoanPrediction':
        cols = ['Gender', 'Married', 'Dependents', 'Education',
                'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        data_dict = dict(zip(cols, input_data))
        return cls(**data_dict)

@app.get("/")
def index():
    return {"message":"Welcome to Loan Prediction App using API - CI CD Jenkins" }

@app.post("/prediction_api")
def predict(loan_details: LoanPrediction):
    data = loan_details.dict()
    prediction = generate_predictions([data])["Prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status":pred}

@app.post("/prediction_ui")
def predict_gui(input_data: List[str]):
    try:
        loan_details = LoanPrediction.from_input_data(input_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    prediction = generate_predictions([loan_details.dict()])["Prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status":pred}