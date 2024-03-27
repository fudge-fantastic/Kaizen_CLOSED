import os
import sys

# This file is inside the MLPackages, so it won't be able to understand wtf is MLPackages
# So we're gonna join the parent path.
path1 = os.getcwd()
path2 = os.path.dirname(path1)
sys.path.append(path2)

import pandas as pd 
import numpy as np
from MLPackages.config import config
from MLPackages.processing.data_handling import load_dataset, save_pipeline
import MLPackages.processing.preprocessing as pp
import MLPackages.pipeline as pipe
import warnings
warnings.filterwarnings('ignore')

def perform_training():
    train_data = load_dataset(config.TRAIN_DATA)
    train_y = train_data[config.TARGET].replace({'Y': 1, 'N': 0})
    pipe.classification_pipeline.fit(train_data[config.FEATURES], train_y)
    save_pipeline(pipe.classification_pipeline)
    
if __name__ =='__main__':
    perform_training()