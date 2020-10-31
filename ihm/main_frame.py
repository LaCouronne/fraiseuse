import tkinter as tk

from ihm.work_config_frame import WorkConfigFrame


root = tk.Tk()
root.title("First_Program")
root.attributes('-fullscreen', 1)

# Creating Menubar
menubar = tk.Menu(root)

# Adding Menu
menubar.add_command(label="New job", command=None)
menubar.add_command(label="Load job", command=None)
root.config(menu=menubar)

form_frame = WorkConfigFrame()

root.mainloop()
