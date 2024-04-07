FROM python:3.11.8

RUN pip install mlflow numpy scipy pandas scikit-learn cloudpickle

COPY train.py .
COPY wine-quality.csv .