# Steps from scratch

---

#### Checkpoint-1
1. Create Virtual Environment
2. Install the mlflow: pip install mlflow
3. Use the command: mlflow ui (to access the UI of MLFlow) and it will grant you a link (local host)
4. Copy paste it into the browser and explore!

#### Checkpoint-2 (for MLProject and python_env file)
Checkout the loan_pred.py and debug.ipynb file to follow the process and know how the logging works in MLFlow. Instead of using loan_pred.py file, we use MLProject.yaml, why? An MLflow Project is a format for packaging data science code in a reusable and reproducible way, based primarily on conventions. In addition, the Projects component includes an API and command-line tools for running projects, making it possible to chain together projects into workflows. 
- Create a MLProject.yaml file, define the parameters (recommended: go through their documentation)
- Create a python_env/conda_env.yaml file and write all dependencies (can be obtained from MLFlow test cases ---> Artifacts)
- Copy paste according to your needs and run the MLProject.yaml file using the commnad: (mlflow run .)
<br>
You might need to install pyenv, follow the below steps: <br>
https://k0nze.dev/posts/install-pyenv-venv-vscode/


#### Checkpoint-3 (for test-model.py)
1. Create a new python file (test-model.py)
2. Goto the mlflow ui and search for the best model logged, goto Atifacts and copy-paste the Prediction code into the file created and run the script
3. Now, try using this command: (mlflow models serve -m (copy-paste the file path you'll find it in the Artifact section) --port 9000)
4. Something like this:
5. mlflow models serve -m file:///D:/MLOps/Orignals/MLOps/MLFlow/mlruns/968621513001670637/5dcff8bf11644b5287deff690ec75a84/artifacts/LogisticRegression 

##### Note:
Make sure to check out the documentation of these below:
- Argparse
- MLFlow  