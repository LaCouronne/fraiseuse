import tkinter as tk
import tkinter.ttk as ttk
import string

from functools import partial

letters = list(string.ascii_uppercase)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
keyboard_keys = letters
keyboard_keys.extend(numbers)
keyboard_keys.extend(['.', '-'])

key_size = 10


class Keyboard(tk.Tk):

    def __init__(self, target, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.title("Virtual Keyboard")
        self.attributes("-topmost", True)
        self.config(bg="black")

        self.target = target

        last_index = 0

        for i, item in enumerate(letters):
            ttk.Button(
                self,
                text=item,
                width=key_size,
                style="W.TButton",
                command=partial(self.type_key, item)
            ).grid(row=i // 7, column=i % 7, ipady=key_size/1.5)
            last_index = i

        ttk.Button(
            self,
            text='⌫',
            style="W.TButton",
            command=self.del_key
        ).grid(row=last_index // 7, column=last_index % 7 + 1, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

        last_index += 2

        ttk.Button(
            self,
            text='⏎',
            style="W.TButton",
            command=self.quit
        ).grid(row=last_index // 7, column=last_index % 7 + 1, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

    def quit(self, *args, **kwargs):
        self.focus()
        self.destroy()

    def type_key(self, key):
        if self.target:
            self.target.insert(tk.INSERT, key)

    def del_key(self, *args, **kwargs):
        if self.target:
            if len(self.target.get()) <= 0:
                return
            self.target.delete(len(self.target.get())-1, tk.END)
