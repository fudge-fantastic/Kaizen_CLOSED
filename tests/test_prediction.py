# Output from the predict.py script shouldn't be null 
# Output from the predict.py script must be in str data type
import pytest
from ..MLPackages.config import config
from ..MLPackages.processing.data_handling import load_dataset
from predict import generate_predictions

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
    assert isinstance(single_prediction.get('prediction')[0], str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get('prediction')[0] == 'Y'