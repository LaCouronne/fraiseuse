import tkinter as tk

from objects.work import Work
from controllers.work_manager import WorkManager

root = tk.Tk()
root.title("First_Program")

# Creating Menubar
menubar = tk.Menu(root)

# Adding Menu
menubar.add_command(label="New job", command=None)
menubar.add_command(label="Load job", command=None)
root.config(menu=menubar)


def get_work_from_parameters():
    work = Work(_, _, _)

    return work


def start_job():
    work = get_work_from_parameters()
    validated = work.validate()


def save_job():
    work = get_work_from_parameters()
    validated = work.validate()


# Barrel form
barrel_label = tk.Label(root, text='Barrel', font=('calibre', 15, 'bold'))
barrel_label.grid(row=0, column=0)

barrel_diameter_var = tk.DoubleVar()
barrel_diameter_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
barrel_diameter_entry = tk.Entry(root, textvariable=barrel_diameter_var, font=('calibre', 10, 'normal'))
barrel_diameter_label.grid(row=1, column=0)
barrel_diameter_entry.grid(row=1, column=1)

barrel_height_var = tk.DoubleVar()
barrel_height_label = tk.Label(root, text='Height', font=('calibre', 10, 'bold'))
barrel_height_entry = tk.Entry(root, textvariable=barrel_height_var, font=('calibre', 10, 'normal'))
barrel_height_label.grid(row=2, column=0)
barrel_height_entry.grid(row=2, column=1)

# Motif form 
motif_label = tk.Label(root, text='Motif', font=('calibre', 15, 'bold'))
motif_label.grid(row=4, column=0)

height_var = tk.DoubleVar()
height_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
height_entry = tk.Entry(root, textvariable=height_var, font=('calibre', 10, 'normal'))
height_label.grid(row=5, column=0)
height_entry.grid(row=5, column=1)

width_var = tk.DoubleVar()
width_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
width_entry = tk.Entry(root, textvariable=width_var, font=('calibre', 10, 'normal'))
width_label.grid(row=6, column=0)
width_entry.grid(row=6, column=1)

nb_copy_var = tk.DoubleVar()
nb_copy_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
nb_copy_entry = tk.Entry(root, textvariable=nb_copy_var, font=('calibre', 10, 'normal'))
nb_copy_label.grid(row=7, column=0)
nb_copy_entry.grid(row=7, column=1)


# Options
sub_btn = tk.Button(root, text='Start job', command=test)
save_btn = tk.Button(root, text='Save job', command=test)

sub_btn.grid(row=8, column=0)
save_btn.grid(row=8, column=1)

root.mainloop()
