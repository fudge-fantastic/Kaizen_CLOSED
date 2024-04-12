import os
import sys
path1 = os.getcwd()
path2 = os.path.dirname(path1)
sys.path.append(path2)

from MLPackages.config import config
from MLPackages.processing.data_handling import load_pipeline, load_dataset
import MLPackages.processing.preprocessing as pp
import pandas as pd
import numpy as np
import MLPackages
import warnings
warnings.filterwarnings('ignore')

SAVED_MODEL_PATH = os.path.join(path2, "trained_models", config.MODEL_SAVED)
classification_pipeline = load_pipeline()

# def generate_predictions(data_input):
#     data = pd.DataFrame(data_input)
#     pred = classification_pipeline.predict(data[config.FEATURES])
#     output = np.where(pred==1, "Y", "N")
#     result = {'prediction': output}
#     return result

def generate_predictions(data):
    test_data = load_dataset(config.TEST_DATA)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    # print(output)
    result = {'Prediction': output.tolist()}
    # result = {'Prediction': output}
    # return output
    return result

if __name__ =='__main__':
    generate_predictions()
