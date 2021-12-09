# Generic Exception
class Error(Exception):
    def __init__(self):
        super().__init__()

    def warning(self):
        return "Error", "Something went wrong."

# When a user tries to divide by 0 
class ZeroDivisionError(Error):
    def __init__(self):
        super().__init__()

    def warning(self):
        return "Error", "Cannot be devided by 0."


# Check if user input has errors 
class ErrorHandler:
    def check_error(self,text):
        if "/0" in text:
            raise ZeroDivisionError()
        eval(text)

    def validate_input(self, text):
        try:
            self.check_error(text)
            return True
        except ZeroDivisionError as e:
            return e.warning()
        except:
            return Error().warning()