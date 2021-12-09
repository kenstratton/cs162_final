import tkinter as tk
import pytest
import os
import sys

# Add the path of the directory one level above to the list of module searching paths
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from calculator.exceptions import *
from calculator.components import *


# Fake for Application
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)
        self.calculator = Calculator()
        self.error_handler = ErrorHandler()

    def process_input(self, user_input):
        if user_input == "=":
            text = self.frame1.get_display_text()
            validation = self.error_handler.validate_input(text)
            if validation == True:
                result = self.calculator.calculate(text)
                self.frame1.set_display_text(result)
            else:
                self.frame1.update_warning(validation)
        else:
            self.frame1.add_input(user_input)


# Preparation of data for tests
@pytest.fixture(scope="module")
def app():
    app = Application()
    yield app

@pytest.fixture(scope="module")
def root():
    root = tk.Tk()
    yield root