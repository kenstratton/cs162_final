import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from calculator.exceptions import *
from calculator.components import *

# Attribute tests
def test_class(root):
    output = LabelOutput(root, "display")
    assert output["font"] == 'Helvetica 45'
    assert output.type == "output"

    input = LabelInput(root, "1", "num")
    assert input.bg == [NUM_BG1, NUM_BG2]
    assert input.type == "input"

def test_process(mocker, app):
    # Whether validating method is called during processing
    calculate = mocker.patch("calculator.components.Calculator.calculate")
    validate_input = mocker.patch("calculator.exceptions.ErrorHandler.validate_input", return_value=True)

    text = app.frame1.get_display_text()
    app.process_input("=")
    calculate.assert_called_once_with(text)
    validate_input.assert_called_once_with(text)

def test_exceptions():
    # Whether exceptions react to an irregular input
    error_handler = ErrorHandler()
    with pytest.raises(ZeroDivisionError):
        error_handler.check_error("3/0")
   
    # Whether exceptions output expectedly
    assert error_handler.validate_input("3/0") == ("Error", "Cannot be devided by 0.")