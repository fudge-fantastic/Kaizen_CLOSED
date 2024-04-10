import mlflow
mlflow.set_tracking_uri(f"file:///D:/MLOps/Orignals/MLOps/MLFlow/mlruns/465030820307055676/3b169120da184d3f9feb530521678c8d/artifacts/LogisticRegression")
logged_model = 'runs:/3b169120da184d3f9feb530521678c8d/artifacts/LogisticRegression'

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

# mlflow models serve -m <artifact_path> --port 9000