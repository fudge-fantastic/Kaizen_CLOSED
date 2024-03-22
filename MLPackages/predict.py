from MLPackages.config import config
from MLPackages.processing.data_handling import load_pipeline, load_dataset
import MLPackages.processing.preprocessing as pp
import pandas as pd
import numpy as np

classification_pipeline = load_pipeline(config.MODEL_SAVED)

def generate_predictions22222(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    result = {'Prediction': output}
    return result

def generate_predictions():
    test_data = load_dataset(config.TRAIN_DATA)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    result = {'Prediction': output}
    return result

if __name__ =='__main__':
    generate_predictions()
