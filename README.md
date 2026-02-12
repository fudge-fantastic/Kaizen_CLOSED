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

## 🎓 What I Learned

Building this project taught me the complete MLOps lifecycle:

1. **Package Development** - How to structure reusable ML code as installable packages
2. **Experiment Management** - Systematic model comparison and tracking with MLFlow
3. **API Design** - Both Flask (simplicity) and FastAPI (performance + features)
4. **Containerization** - Isolating dependencies and creating reproducible environments
5. **CI/CD** - Automating the entire deployment pipeline
6. **Production Thinking** - Writing code that's maintainable, testable, and deployable

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
