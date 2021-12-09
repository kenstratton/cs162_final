import tkinter as tk

FONT1 = ("Helvetica", 45)
FONT2 = ("Helvetica", 20)
FONT3 = ("Helvetica", 12)
FG = "#ffffff"

OPT_BG1 = "#444444"
OPT_BG2 = "#666666"
NUM_BG1 = "#666666"
NUM_BG2 = "#888888"
OPE_BG1 = "#00ff00"
OPE_BG2 = "#32cd32"


# Generic class for Label
class Label(tk.Label):
    def __init__(self, root, text, font=None, anchor=None, bg=None):
        super().__init__(
            root,
            text=text,
            font=font,
            anchor=anchor,
            fg=FG,
            bg=bg
        )

    # Locate Label with pack()
    def lbl_pack(self, padx=(0,0), fill="both"):
        self.pack(padx=padx, fill=fill)

    # Lpcate Label with grid() 
    def lbl_grid(self, row, colmun):
        self.grid(
            row=row,
            column=colmun,
            padx=(0,1),
            pady=(0,1)
        )


# Label for an output display and a warning area
class LabelOutput(Label):
    def __init__(self, root, type):
        if type == "display":
            font = FONT1
        else:
            font = FONT3
        super().__init__(root, "", font, tk.E)
        self.type = "output"


# Label for user input
class LabelInput(Label):
    def __init__(self, root, text, type):
        # Change background color up to a role
        if type == "num":
            self.bg = [NUM_BG1, NUM_BG2]
        elif type == "opt":
            self.bg = [OPT_BG1, OPT_BG2]
        elif type == "ope":
            self.bg = [OPE_BG1, OPE_BG2]

        super().__init__(root, text, FONT2, tk.CENTER, self.bg[0])
        self.type = "input"

        self.config(width=6, height=3)
        self.bind("<ButtonPress>", self.bg_press)
        self.bind("<ButtonRelease>", self.bg_release)

    # Change background color when pressed
    def bg_press(self, evnt):
        self.config(bg=self.bg[1])

    # Turn the color back to origiral when released
    def bg_release(self, evnt):
        self.config(bg=self.bg[0])


# Calculator Output
class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lbl_warning = LabelOutput(self, "warning")
        self.lbl_display = LabelOutput(self, "display")
        self.lbl_warning.lbl_pack((0,5))
        self.lbl_display.lbl_pack((0,8))

    # Get a text on an output display 
    def get_display_text(self):
        text = self.lbl_display["text"]
        return text

    # Set a text on an output display 
    def set_display_text(self, text):
        self.lbl_display.config(text=text)

    # Add a text to the existing text
    def add_display_text(self, text):
        pre_text = self.get_display_text()
        self.lbl_display.config(text=pre_text+text)

    # Set a text on a warning display 
    def set_warning_text(self, text):
        self.lbl_warning.config(text=text)

    # Set or remove Error messages
    def update_warning(self, message=None):
        if message:
            self.set_display_text(message[0])
            self.set_warning_text(message[1])
        elif self.get_display_text() == "Error":
            self.set_display_text("")
            self.set_warning_text("")

    # Switch input to texts which Calculator can operate
    def add_input(self, val):
        # When C is pushed
        if val == "C":
            self.set_display_text("")
        # When x is pushed
        elif val == "x":
            self.add_display_text("*")
        # When - is pushed
        elif val == "ー":
            self.add_display_text("-")
        # When + is pushed
        elif val == "＋":
            self.add_display_text("+")
        # When / or Numbers are pushed
        else:
            self.add_display_text(val)


# User Input (Number, Operand, and Clear button)
class Frame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Number (0 ~ 9)
        self.lbl_num_list = []
        for i in range(10):
            self.lbl_num_list.append(LabelInput(self, str(i), "num"))
        # Clear button (C)
        self.lbl_clear = LabelInput(self, "C", "opt")
        self.lbl_eql = LabelInput(self, "=", "ope")
        # Operands (/, x, -, +)
        self.lbl_div = LabelInput(self, "/", "ope")
        self.lbl_mult = LabelInput(self, "x", "ope")
        self.lbl_minus = LabelInput(self, "ー", "ope")
        self.lbl_plus = LabelInput(self, "＋", "ope")
        # The first row (7, 8, 9, /)
        self.lbl_num_list[7].lbl_grid(0, 0)
        self.lbl_num_list[8].lbl_grid(0, 1)
        self.lbl_num_list[9].lbl_grid(0, 2)
        self.lbl_div.lbl_grid(0, 3)
        # The second row (4, 5, 6, x)
        self.lbl_num_list[4].lbl_grid(1, 0)
        self.lbl_num_list[5].lbl_grid(1, 1)
        self.lbl_num_list[6].lbl_grid(1, 2)
        self.lbl_mult.lbl_grid(1, 3)
        # The Third row (1, 2, 3, -)
        self.lbl_num_list[1].lbl_grid(2, 0)
        self.lbl_num_list[2].lbl_grid(2, 1)
        self.lbl_num_list[3].lbl_grid(2, 2)
        self.lbl_minus.lbl_grid(2, 3)
        # The Forth row (0, C, =, +)
        self.lbl_num_list[0].lbl_grid(3, 0)
        self.lbl_clear.lbl_grid(3, 1)
        self.lbl_eql.lbl_grid(3, 2)
        self.lbl_plus.lbl_grid(3, 3)


# Calculate and return the result
class Calculator:
    def calculate(self, text):
        return str(eval(text))