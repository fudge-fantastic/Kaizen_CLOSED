# Output from the predict.py script shouldn't be null 
# Output from the predict.py script must be in str data type
# After successfully completing the file structure, make sure to run the command: pytest or pytest -v

import sys
import pytest
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_dir)
import MLPackages
path = os.path.dirname(MLPackages.__file__)
sys.path.append(path)

from MLPackages.config import config
from MLPackages.processing.data_handling import load_dataset
from MLPackages.predict import generate_predictions

# Fixtures ---> Functions before the test function ---> Ensure single_prediction works 
# Marking important function as a fixture

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_DATA)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

# Checks if the output is not None
def test_single_pred_isnot_none(single_prediction):
    assert single_prediction is not None

# Checks if the output is string data-type
def test_single_pred_is_str_type(single_prediction):
    assert isinstance(single_prediction.get('Prediction')[0], str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get('Prediction')[0] == 'Y'
