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

    def lbl_pack(self, padx=(0,0), fill="both"):
        self.pack(padx=padx, fill=fill)

    def lbl_grid(self, row, colmun):
        self.grid(
            row=row,
            column=colmun,
            padx=(0,1),
            pady=(0,1)
        )

class LabelOutput(Label):
    def __init__(self, root, type):
        if type == "display":
            font = FONT1
        else:
            font = FONT3
        super().__init__(root, "", font, tk.E)
        self.type = "output"


class LabelInput(Label):
    def __init__(self, root, text, type):
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

    def bg_press(self, evnt):
        self.config(bg=self.bg[1])

    def bg_release(self, evnt):
        self.config(bg=self.bg[0])