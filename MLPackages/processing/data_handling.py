import os 
import pandas as pd
import joblib  
from MLPackages.config import config

def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(filepath)
    return _data

# Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVED_MODEL_PATH, config.MODEL_SAVED)
    # Pipeline to be saved in the same directory
    joblib.dump(pipeline_to_save, save_path)
    print(f"The {config.MODEL_SAVED} has been saved")

# Deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVED_MODEL_PATH, config.MODEL_SAVED)
    # Pipeline to be loaded from the same directory
    model_loaded = joblib.load(pipeline_to_load, save_path)
    print("The model has been loaded")
    return model_loaded