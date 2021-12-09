from components import *
from exceptions import *

WINDOW_W = 315
WINDOW_H = 380
WINDOW_BG = "#222222"


# Set up GUI
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # Title, Background color, and Window size
        self.title("Calculator")
        self.config(bg=WINDOW_BG)
        self.geometry(f"{WINDOW_W}x{WINDOW_H}")

        # Frame1 -> output display. Frame2 -> input area
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)
        self.frame1.pack(fill="both")
        self.frame2.pack()

        # CalcHandler -> calculate. ErrorHandler -> handle erroes
        self.calculator = Calculator()
        self.error_handler = ErrorHandler()

        # Set all InputLabels to call a method
        self.bind_class("Label", "<ButtonRelease>", self.get_widget)

    def get_widget(self, evnt):
        wg = evnt.widget
        user_input = wg["text"]
        print(user_input)
        self.process_input(user_input)

    def process_input(self, user_input):
        # Validate and calculate input
        self.frame1.update_warning()
        if user_input == "=":
            text = self.frame1.get_display_text()
            validation = self.error_handler.validate_input(text)
            # True -> calculate
            if validation == True:
                result = self.calculator.calculate(text)
                self.frame1.set_display_text(result)
            # Any error -> notice warning
            else:
                self.frame1.update_warning(validation)
        # Add input text to the existing display text
        else:
            self.frame1.add_input(user_input)


if __name__ == "__main__":
    app = Application()
    app.mainloop()