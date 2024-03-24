import os
import sys
path1 = os.getcwd()
path2 = os.path.dirname(path1)
path3 = os.path.dirname(path2)
sys.path.append(path3)

# def if_working():
#     path3 = print(os.path.dirname(path2))
#     return path3

# if __name__ == '__main__':
#     if_working()

import pandas as pd
import joblib  
import MLPackages
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
    print(f"The has been saved and named as: {config.MODEL_SAVED}")

# Deserialization
def load_pipeline():
    npath1 = os.path.dirname(MLPackages.__file__)
    save_path = os.path.join(npath1, 'trained_models', config.MODEL_SAVED)
    # save_path = os.path.join(config.SAVED_MODEL_PATH, config.MODEL_SAVED)
    # Pipeline to be loaded from the same directory
    model_loaded = joblib.load(save_path)
    print(f"The {config.MODEL_SAVED} model has been loaded")
    return model_loaded



# def if_working():
#     word = print("Working well without import errors")
#     return word

# if __name__ == '__main__':
#     if_working()