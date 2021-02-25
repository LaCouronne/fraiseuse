import tkinter as tk
import tkinter.ttk as ttk
from pynput.keyboard import Key, Controller
import string

from functools import partial

letters = list(string.ascii_uppercase)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# style = ttk.Style()
# style.configure("W.TButton", font=("calibri", 10, "bold"), foreground="red", background="black")
#
# typer = Controller()


class Keyboard(tk.Tk):

    def __init__(self, linked_input, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.linked_input = linked_input

        self.title("Virtual Keyboard")
        self.attributes("-topmost", True)
        self.config(bg="black")

        self.bind('<FocusOut>', self.quit)

        for i, item in enumerate(letters):
            ttk.Button(
                self,
                text=item,
                width=5,
                style="W.TButton",
                command=partial(self.type_key, item)
            ).grid(row=i // 7, column=i % 7)

    def quit(self):
        self.focus()
        self.destroy()

    def type_key(self, key):
        print(str(key))  # test line
        self.linked_input.insert(tk.INSERT, key)
