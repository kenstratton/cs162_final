from components import *
from exceptions import *

WINDOW_W = 315
WINDOW_H = 380
WINDOW_BG = "#222222"

MEMORY = 0

class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lbl_warning = LabelOutput(self, "warning")
        self.lbl_display = LabelOutput(self, "display")
        self.lbl_warning.lbl_pack((0,5))
        self.lbl_display.lbl_pack((0,8))

class Frame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lbl_num_list = []
        for i in range(10):
            self.lbl_num_list.append(LabelInput(self, str(i), "num"))
        self.lbl_clear = LabelInput(self, "C", "opt")
        self.lbl_eql = LabelInput(self, "=", "ope")
        self.lbl_div = LabelInput(self, "/", "ope")
        self.lbl_mult = LabelInput(self, "x", "ope")
        self.lbl_minus = LabelInput(self, "ー", "ope")
        self.lbl_plus = LabelInput(self, "＋", "ope")
        self.lbl_num_list[7].lbl_grid(0, 0)
        self.lbl_num_list[8].lbl_grid(0, 1)
        self.lbl_num_list[9].lbl_grid(0, 2)
        self.lbl_div.lbl_grid(0, 3)
        self.lbl_num_list[4].lbl_grid(1, 0)
        self.lbl_num_list[5].lbl_grid(1, 1)
        self.lbl_num_list[6].lbl_grid(1, 2)
        self.lbl_mult.lbl_grid(1, 3)
        self.lbl_num_list[1].lbl_grid(2, 0)
        self.lbl_num_list[2].lbl_grid(2, 1)
        self.lbl_num_list[3].lbl_grid(2, 2)
        self.lbl_minus.lbl_grid(2, 3)
        self.lbl_num_list[0].lbl_grid(3, 0)
        self.lbl_clear.lbl_grid(3, 1)
        self.lbl_eql.lbl_grid(3, 2)
        self.lbl_plus.lbl_grid(3, 3)

class CalcHandler:
    def __init__(self, master, frame1, frame2, error_handler):
        self.master = master
        self.frame1 = frame1
        self.frame2 = frame2
        self.e_handler = error_handler

        master.bind_class("Label", "<ButtonRelease>", self.handle_calc)

    def handle_calc(self, evnt):
        wg = evnt.widget
        self.update_warning()
        if wg.type == "input":
            txt = self.frame1.lbl_display["text"]
            if wg["text"] == "C":
                self.frame1.lbl_display.config(text="")
            elif wg["text"] == "=":
                zero_div = self.e_handler.evaluate_division(txt)
                oper_end = self.e_handler.evaluate_operand(txt)
                if zero_div:
                    self.update_warning(zero_div)
                elif oper_end:
                    self.update_warning(oper_end)
                else:
                    result = str(eval(txt))
                    self.frame1.lbl_display.config(text=result)
            elif wg["text"] == "x":
                self.frame1.lbl_display.config(text=txt+"*")
            elif wg["text"] == "ー":
                self.frame1.lbl_display.config(text=txt+"-")
            elif wg["text"] == "＋":
                self.frame1.lbl_display.config(text=txt+"+")
            else:
                self.frame1.lbl_display.config(text=txt+wg["text"])

    def update_warning(self, message=None):
        if message:
            self.frame1.lbl_display.config(text=message[0])
            self.frame1.lbl_warning.config(text=message[1])
        elif self.frame1.lbl_display["text"] == "Error":
            self.frame1.lbl_display.config(text="")
            self.frame1.lbl_warning.config(text="")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.config(bg=WINDOW_BG)
        self.geometry(f"{WINDOW_W}x{WINDOW_H}")

        frame1 = Frame1(self)
        frame2 = Frame2(self)
        frame1.pack(fill="both")
        frame2.pack()

        CalcHandler(self, frame1, frame2, ErrorHandler())

if __name__ == "__main__":
    app = Application()
    app.mainloop()