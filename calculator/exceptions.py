class Error(Exception):
    def __init__(self):
        super().__init__()

    def warning(self, lbl1):
        return "Error"

class ZeroDivisionError(Error):
    def __init__(self):
        super().__init__()

    def warning(self):
        return "Error", "Cannot be devided by 0."

class OperandEndError(Error):
    def __init__(self):
        super().__init__()

    def warning(self):
        return "Error", "Cannot be ended with an operand."

class ErrorHandler:
    def evaluate_division(self, text):
        try:
            if "/0" in text:
                raise ZeroDivisionError()
            else:
                return None
        except ZeroDivisionError as e:
            return e.warning()

    def evaluate_operand(self, text):
        try:
            if text[-1] in ["+", "-", "*", "/"]:
                raise OperandEndError()
            else:
                return None
        except OperandEndError as e:
            return e.warning()