from MLPackages.config import config
from MLPackages.processing.data_handling import load_pipeline, load_dataset
import MLPackages.processing.preprocessing as pp
import pandas as pd
import numpy as np
import pathlib
import MLPackages
import os
import warnings
warnings.filterwarnings('ignore')

new_path = pathlib.Path(MLPackages.__file__).resolve().parent
SAVED_MODEL_PATH = os.path.join(new_path, "trained_models", config.MODEL_SAVED)
classification_pipeline = load_pipeline()

def generate_predictions(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    result = {'prediction': output}
    return result

# def generate_predictions():
#     test_data = load_dataset(config.TEST_DATA)
#     pred = classification_pipeline.predict(test_data[config.FEATURES])
#     output = np.where(pred==1, "Y", "N")
#     print(output)
#     # result = {'Prediction': output}
#     return output

if __name__ =='__main__':
    generate_predictions()
