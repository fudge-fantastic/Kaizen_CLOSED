# Steps from scratch

---

#### Checkpoint-1 
1. Create Virtual Environment
2. Install the mlflow: pip install mlflow
3. Use the command: mlflow ui (to access the UI of MLFlow) and it will grant you a link (local host)
4. Copy paste it into the browser and explore!
5. (stats: success)

#### Checkpoint-2 (for MLProject and python_env file)
Checkout the loan_pred.py and debug.ipynb file to follow the process and know how the logging works in MLFlow. Instead of using loan_pred.py file, we use MLProject.yaml, why? An MLflow Project is a format for packaging data science code in a reusable and reproducible way, based primarily on conventions. In addition, the Projects component includes an API and command-line tools for running projects, making it possible to chain together projects into workflows. 
- Create a MLProject.yaml file, define the parameters (recommended: go through their documentation)
- Create a python_env/conda_env.yaml file and write all dependencies (can be obtained from MLFlow test cases ---> Artifacts)
- Copy paste according to your needs and run the MLProject.yaml file using the commnad: (mlflow run .)
- You might need to install pyenv (make sure to restart the PC/Laptop): https://k0nze.dev/posts/install-pyenv-venv-vscode/
- After successful installation, don't forget to setup the 'PYENV_ROOT' path, for instance: export PYENV_ROOT="C:\Users\owner\.pyenv\pyenv-win"
- Make sure you use the experiment name too: mlflow run . --experiment-name "Loan_Prediction"
- (stats: success)


#### Checkpoint-3 (for test-model.py)
1. Create a new python file (test-model.py)
2. Goto the mlflow ui and search for the best model logged, goto Atifacts and copy-paste the Prediction code into the file created and run the script
3. Now, try using this command: (mlflow models serve -m (copy-paste the file path you'll find it in the Artifact section) --port 9000)
4. Something like this:
5. mlflow models serve -m D:/MLOps/Orignals/MLOps/MLFlow/mlruns/968621513001670637/5dcff8bf11644b5287deff690ec75a84/artifacts/LogisticRegression --port 9000
6. [LOG: IOError: [Errno 13] Permission denied] How to resolve? Run the VSCode or Terminal as Administrator.
7. Rerun the command that raised the error, install postman.
8. Goto postman, instead of GET use POST and copy paste Server ID (for example-  http://127.0.0.1:9000/invocations). Now goto Body and select raw radio button and select the format as JSON, beutify and click SEND button
9. You can also use http://localhost:9000
10. You can also use the following code in GitBash 
11. (stats: success)

``` 
curl --location 'http://127.0.0.1:9000/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "dataframe_split": {
        "columns": [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ],
        "data": [
            [
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
            ]
        ]
    }
}' 
```
#### Checkpoint-4 (Log Model metrics in MySQL)
1. pip install mysqlclient in Venv
2. mlflow server --host 0.0.0.0 --port 5001 --backend-store-uri mysql://username:password@localhost (---> address to connect to your database)/schema_name --default-artifact-root $PWD/mlruns or mlflow server --backend-store-uri mysql+pymysql://(username):(password)@(host):(port)/(database) --host 0.0.0.0
3. Just in case if you wanna change your MySQL server password, Search for MySQL Server directory and open bin folder, click on address bar and type cmd, then use command: mysqladmin -u root -p password (new_password). After hitting enter, enter the old password to update the password.
4. Now goto your loan_pred.py file and set the tracking URI as (http://0.0.0.0:5001) which will be given after executing that command in the 2nd point.
5. Uncomment mlflow.set_tracking_uri("http://0.0.0.0:5001/") in the loan_pred.py file and run it.
6. mlflow server --host 0.0.0.0 --port 5001 --backend-store-uri mysql://root:bluesalt123@localhost/db_mlflow --default-artifact-root $PWD/mlruns
7. mlflow server --backend-store-uri mysql+pymysql://root:bluesalt123@localhost/db_mlflow --default-artifact-root $PWD/mlruns -h 0.0.0.0 -p 5000 (this worked!)
8. NOTE: The --default-artifact-root is a directory for storing artifacts for every new experiment

#### Checkpoint-5 (Registring the model)
1. Choose any random run_id from the mlflow ui (can be found in artifacts section)
2. Click Register the Model (and create new model with your choice of name)
3. Choose the Stage of your choice, for now choose Staging (deprecated)
4. Needs to be practiced more!