import mlflow
import warnings
warnings.filterwarnings('ignore')
mlflow.set_tracking_uri(f"file:///D:/MLOps/Orignals/MLOps/MLFlow/mlruns/968621513001670637/5dcff8bf11644b5287deff690ec75a84/artifacts/LogisticRegression")
logged_model = 'runs:/5dcff8bf11644b5287deff690ec75a84/LogisticRegression'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
data = [[
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]]
print(f"Prediction is : {loaded_model.predict(pd.DataFrame(data))}")