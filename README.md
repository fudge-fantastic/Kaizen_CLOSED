# Kaizen (改善) - End-to-End MLOps Pipeline for Loan Prediction

> *Kaizen* means "continuous improvement" in Japanese - a fitting name for this project where I learned and implemented a complete ML deployment pipeline from scratch.

## 📋 Project Overview

This project represents my journey through building a production-ready machine learning system. I developed a **loan prediction model** and took it from a Jupyter notebook to a fully deployable, containerized application with automated CI/CD pipelines. The goal was to understand every piece of the MLOps puzzle - from model development to production deployment.

## 🎯 What I Built

This isn't just a machine learning model - it's a complete production-grade ML system with:

- **Custom Python Package** (`MLPackages v1.0.0`) - A fully installable package with proper structure
- **MLFlow Integration** - Experiment tracking with multiple model comparisons
- **Dual API Implementation** - Both Flask and FastAPI endpoints for serving predictions
- **Docker Containerization** - Multiple containerized components for different services
- **CI/CD Pipeline** - Automated testing and deployment with Jenkins
- **Comprehensive Testing** - Unit tests for prediction pipeline

## ⚡ Quick Start

**Prerequisites**: Python 3.9+, pip

### Option 1: Run FastAPI App (Fastest Way to See It Work)
```bash
# Clone the repository
git clone <repository-url>
cd Kaizen_CLOSED

# Install dependencies
cd FastAPI
pip install fastapi uvicorn scikit-learn pandas numpy joblib

# Run the API server
python loan_pred_fastapi_app.py

# Visit http://127.0.0.1:8000/docs for interactive API documentation
```

### Option 2: Install & Use the ML Package
```bash
cd Package
pip install -e .

# Train the model
python MLPackages/training_pipeline.py

# Run tests
pytest tests/
```

### Option 3: Explore MLFlow Experiments
```bash
# Install MLFlow
pip install mlflow scikit-learn pandas numpy matplotlib

# Start MLFlow UI
mlflow server --host localhost --port 5000

# In another terminal, run experiments
cd MLFlow
python loan_pred.py

# View experiments at http://localhost:5000
```

## 🏗️ Project Structure

```
Kaizen_CLOSED/
├── Package/              # Production-ready ML package
│   ├── MLPackages/      # Main package module
│   │   ├── config/      # Configuration management
│   │   ├── datasets/    # Training and test data
│   │   ├── processing/  # Data preprocessing modules
│   │   ├── trained_models/  # Saved model artifacts
│   │   ├── pipeline.py  # ML pipeline definition
│   │   ├── predict.py   # Prediction interface
│   │   └── training_pipeline.py
│   ├── tests/           # Unit tests
│   └── setup.py         # Package installation script
│
├── MLFlow/              # Experiment tracking & model comparison
│   ├── loan_pred.py     # MLFlow experiment with 4 models
│   ├── basic_mlflow.py  # MLFlow basics
│   └── test-model.py    # Model evaluation
│
├── Flask/               # Flask API implementation
│   ├── flask_loanpred.py
│   ├── app.py
│   └── templates/       # HTML templates
│
├── FastAPI/             # FastAPI implementation
│   ├── loan_pred_fastapi_app.py  # Main FastAPI app
│   └── pydantic-demo.py          # Data validation demo
│
├── Docker/              # Containerization
│   ├── docker-loan-prediction/   # Training container
│   ├── docker-mlflow/            # MLFlow server container
│   └── flask-app/                # Flask app container
│
└── Jenkins/             # CI/CD pipeline
    ├── src/MLPackages/  # Package for Jenkins deployment
    └── tests/           # Integration tests
```

## 🚀 Key Features

### 1. **Production-Ready ML Package**
I built `MLPackages` as an installable Python package following best practices:
- Modular design with clear separation of concerns
- Configuration management for easy environment switching
- Custom preprocessing pipeline with:
  - Categorical and numerical imputation
  - Log transformation for handling outliers
  - Feature engineering (TotalIncome creation)
  - Label encoding for categorical variables
- Pickle-based model persistence

### 2. **MLFlow Experiment Tracking**
Implemented comprehensive experiment tracking comparing 4 classification algorithms:
- Logistic Regression
- Decision Tree Classifier
- Gradient Boosting Classifier
- AdaBoost Classifier

Each experiment logs:
- Accuracy, Precision, Recall, F1-Score, AUC metrics
- ROC curve visualizations
- Model artifacts for reproducibility
- Connected to local MLFlow tracking server

### 3. **Dual API Deployment**

**Flask Implementation:**
- Simple and lightweight
- HTML template rendering for web interface
- RESTful endpoints for predictions

**FastAPI Implementation:**
- Modern async Python framework
- Automatic API documentation (Swagger UI)
- Pydantic models for request validation
- Type hints throughout

Both APIs serve the RandomForest model trained on preprocessed loan data.

### 4. **Docker Containerization**
Created separate containers for:
- **Model Training**: Isolated environment for training pipeline
- **MLFlow Server**: Experiment tracking backend
- **Flask API**: Production API server

Each Dockerfile is optimized with:
- Python 3.11 base image
- Proper dependency management
- Executable permissions
- Clean ENTRYPOINT/CMD structure

### 5. **CI/CD with Jenkins**
Set up automated pipeline for:
- Running unit tests on every commit
- Building and testing the package
- Automated deployment triggers
- Integration with GitHub webhooks

## 🔬 The ML Model

**Problem**: Predict loan approval status based on applicant information

**Features Used**:
- Gender, Marital Status, Dependents
- Education, Employment Status
- Applicant Income, Co-applicant Income
- Loan Amount, Loan Term
- Credit History, Property Area

**Preprocessing Pipeline**:
1. Handle missing values (mode for categorical, median for numerical)
2. Log transform income and loan amount (reduce skewness)
3. Feature engineering - combine applicant and co-applicant income
4. Encode categorical variables
5. Train RandomForest classifier

**Model Performance**: Tracked using MLFlow with multiple metrics and ROC curves

## 🛠️ Technologies Used

- **ML/Data Science**: pandas, numpy, scikit-learn
- **Experiment Tracking**: MLFlow
- **API Frameworks**: Flask, FastAPI, Uvicorn
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Testing**: pytest
- **Model Serialization**: joblib, pickle
- **Validation**: Pydantic

## 📦 Installation & Usage

### Install the Package
```bash
cd Package
pip install -e .
```

### Train the Model
```bash
python MLPackages/training_pipeline.py
```

### Run MLFlow Experiments
```bash
# Start MLFlow server
mlflow server --host localhost --port 5000

# Run experiments
cd MLFlow
python loan_pred.py
```

### Start FastAPI Server
```bash
cd FastAPI
python loan_pred_fastapi_app.py
# Access API docs at: http://127.0.0.1:8000/docs
```

### Run with Docker
```bash
cd Docker/docker-loan-prediction
docker build -t loan-prediction .
docker run loan-prediction
```

## 🧪 Testing
```bash
cd Package
pytest tests/test_prediction.py
```

## 📊 API Usage Example

**FastAPI Prediction Request**:
```python
{
  "Gender": 1.0,
  "Married": 0.0,
  "Dependents": 0.0,
  "Education": 0.0,
  "Self_Employed": 0.0,
  "LoanAmount": 4.98745,
  "Loan_Amount_Term": 360.0,
  "Credit_History": 1.0,
  "Property_Area": 2.0,
  "TotalIncome": 8.698
}
```

**Response**:
```json
{
  "Status of Loan Application": "Approved"
}
```

## 🔧 Implementation Details

### ML Package (`Package/`)

The `MLPackages` package (v1.0.0) is structured as a proper Python installable package via `setup.py`. It contains:

**Configuration (`config/config.py`)**
- Centralizes all paths (data, model artifact) and feature definitions
- Defines 11 input features split into numeric (`ApplicantIncome`, `LoanAmount`, `Loan_Amount_Term`) and categorical (`Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`, `Credit_History`, `Property_Area`)
- Declares `FEATURE_TO_MODIFY` (`ApplicantIncome`) and `FEATURE_TO_DROP` (`CoapplicantIncome`) for feature engineering
- Model artifact saved to `MLPackages/trained_models/classification_model.pkl`

**Custom Preprocessing Transformers (`processing/preprocessing.py`)**

7 custom classes, all inheriting from scikit-learn's `BaseEstimator` and `TransformerMixin`:

| Transformer | Purpose |
|---|---|
| `MeanImputer` | Fills missing numeric values with computed mean per column |
| `ModeImputer` | Fills missing categorical values with mode per column |
| `DomainProcessing` | Feature engineering — adds `CoapplicantIncome` into `ApplicantIncome` |
| `DropColumns` | Drops `CoapplicantIncome` after income combination |
| `CustomLabelEncoder` | Encodes categoricals by mapping value → integer based on sorted value counts |
| `LogTransformer` | Applies `np.log()` to specified numeric features to reduce skew |
| `MinMaxScaler` (sklearn) | Normalizes numeric features to [0, 1] range |

**Scikit-learn Pipeline (`pipeline.py`)**

Assembles all 7 transformers plus the final RandomForest model into a single `Pipeline` object — ensuring preprocessing and prediction are always applied consistently. The pipeline is serialized with `joblib` on training and deserialized on inference.

**Training Pipeline (`training_pipeline.py`)**

`perform_training()` loads `train.csv`, maps `Loan_Status` (Y→1, N→0), fits the full pipeline on the 11 features, and persists the pipeline artifact.

**Prediction Module (`predict.py`)**

`generate_predictions()` loads the serialized pipeline, runs it on test data, and maps predictions back to readable labels (1→"Y", 0→"N").

**Data Handling (`processing/data_handling.py`)**

`load_dataset()`, `save_pipeline()`, and `load_pipeline()` abstract all I/O behind simple function calls so training/prediction code stays clean.

---

### MLFlow Experiment Tracking (`MLFlow/`)

**Setup**: Local MLFlow tracking server at `http://localhost:5000`, experiment named `"Loan_Prediction"`.

**Model Comparison (`loan_pred.py`)**

Trains and compares 4 classifiers on an 70/30 train-test split (`random_state=21`):
- `LogisticRegression` (`max_iter=1000`)
- `DecisionTreeClassifier`
- `GradientBoostingClassifier`
- `AdaBoostClassifier` (`algorithm='SAMME'`)

Each run logs: **Accuracy, Precision, Recall, F1-Score, AUC** — plus a ROC curve PNG artifact (`plots/ROC_curve.png`) generated with matplotlib.

**Preprocessing inside MLFlow scripts**: Categorical/numeric imputation (most_frequent / median) → log transform on income and loan columns → `TotalIncome = ApplicantIncome + CoapplicantIncome` feature engineering → label encoding — mirrors the package pipeline approach but implemented inline.

**Basic MLFlow Demo (`basic_mlflow.py`)**: Demonstrates parameterized runs using the UCI wine quality dataset with ElasticNet regression, logging `alpha`, `l1_ratio`, RMSE, MAE, and R².

**Refactored Version (`script.py`)**: Improved design with helper functions — `preprocess_data()`, `split_data()`, `train_models()`, `eval_metrics()`, `mlflow_logging()` — for cleaner separation of concerns.

---

### Flask API (`Flask/`)

**Endpoints** (`app.py`):

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Serves `homepage.html` — HTML form for user input |
| `POST` | `/predict` | Accepts form data, runs prediction, renders result |

**Prediction flow**: Form data parsed → `First_Name`/`Last_Name` stripped → all values cast to `int` → `TotalIncome = log(ApplicantIncome + CoapplicantIncome)` computed → 10-feature array fed to `RF_Loan_model.pkl` → approval/rejection string rendered in template.

**HTML Form** (`templates/homepage.html`): Covers all 12 input fields — text inputs for income/loan fields, radio buttons for binary/categorical fields (Gender, Married, Education, Self_Employed, Credit_History, Property_Area).

**Error handling**: Custom 404 and 500 handlers configured. Server binds to `0.0.0.0:80`.

---

### FastAPI (`FastAPI/`)

**Pydantic Model** (`LoanPred`): Validates all 10 post-processed features as `float` — `Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`, `LoanAmount`, `Loan_Amount_Term`, `Credit_History`, `Property_Area`, `TotalIncome`.

**Endpoints** (`loan_pred_fastapi_app.py`):

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | `{"message": "Welcome to Loan Prediction App"}` |
| `POST` | `/predict` | JSON body → prediction → `{"Status of Loan Application": "Approved"\|"Rejected"}` |

**Prediction flow**: JSON parsed to dict → feature values extracted in fixed order → numpy array constructed → `RF_Loan_model.pkl` inference → 0/1 mapped to "Rejected"/"Approved".

**Jenkins variant** (`Jenkins/main.py`): Extended FastAPI app with CORS middleware (all origins allowed), accepts string inputs for categorical features, and exposes two additional endpoints — `/prediction_api` (JSON body) and `/prediction_ui` (query parameters) — both calling `generate_predictions()` from the installed `MLPackages`.

**Auto-generated docs**: Available at `http://127.0.0.1:8000/docs` (Swagger UI) and `/redoc`.

---

### Docker Containerization (`Docker/`)

Four distinct container definitions, each with Python 3.11 base images:

**Training Container** (`docker-loan-prediction/`):
- Base: `python:3.11.8`
- Copies source → installs `requirements.txt` → sets executable permissions
- Entrypoint: `docker_train.py` (trains RandomForest, outputs `RF_Loan_model.pkl`)
- Runs as a batch job (no exposed ports)

**MLFlow Server Container** (`docker-mlflow/`):
- Base: `python:3.11.8`
- Installs: `mlflow`, `numpy`, `scipy`, `pandas`, `scikit-learn`, `cloudpickle`
- Bundles wine quality dataset and training script
- Intended to serve the MLFlow tracking server (port 5000)

**Flask API Container** (`flask-app/`):
- Base: `python:3.11.8`
- Workdir: `/usr/src/app`
- `pip install --no-cache-dir` for smaller image layers
- `EXPOSE 5000` → `CMD ["python", "./app.py"]`

**Jenkins Deployment Container** (`Jenkins/Dockerfile`):
- Base: `python:3.11-slim-buster` (slim for smaller footprint)
- System deps: `build-essential`, `libpq-dev` (build tools + PostgreSQL support)
- Installs package from `src/` directory: `pip install src/.`
- `EXPOSE 8000` → `CMD ["python", "main.py"]`

**Docker Compose** (`Jenkins/docker-compose.yaml`): Single-service compose file mapping `image12` / `container12` on host port 8000 → container port 8000.

---

### CI/CD with Jenkins (`Jenkins/`)

The Jenkins integration directory bundles a self-contained deployment unit:
- A copy of `MLPackages` under `src/` — installed inside the container via `pip install src/.`
- The extended `main.py` FastAPI app that imports from the installed package
- A `Dockerfile` for containerized deployment
- `docker-compose.yaml` for orchestration
- Test suite under `src/tests/` run during the pipeline

The pipeline connects to GitHub webhooks to trigger automated test → build → deploy cycles on every commit. The container approach ensures environment consistency between Jenkins builds and production.

---

### Testing (`Package/tests/`, `Jenkins/src/tests/`)

Uses `pytest` with fixtures. The fixture loads the test dataset, runs `generate_predictions()` on the first row, and three test cases validate the result:

| Test | Assertion |
|---|---|
| `test_single_pred_isnot_none` | Output is not `None` |
| `test_single_pred_is_str_type` | Prediction value is a `str` |
| `test_single_pred_validate` | Prediction equals `'Y'` for the known test row |

Tests require the model to be trained and serialized beforehand, making them integration-level checks of the full pipeline.

## 🔮 Future Improvements

While this project is feature-complete for a learning exercise, here are potential enhancements:
- Add model versioning and A/B testing
- Implement monitoring and logging (Prometheus/Grafana)
- Add database integration for predictions history
- Deploy to cloud platforms (AWS/GCP/Azure)
- Implement model retraining pipeline
- Add data drift detection

## 📝 License

MIT License - Feel free to use this for learning!

---

**Author**: Bluesalt
**Email**: adi.pandagle@gmail.com
**GitHub**: [@fudge-fantastic](https://github.com/fudge-fantastic)

*This project represents continuous improvement (改善) in my ML engineering skills.*
