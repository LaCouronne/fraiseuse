import tkinter as tk

from objects.work import Work
from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template

root = tk.Tk()
root.title("First_Program")

# Creating Menubar
menubar = tk.Menu(root)

# Adding Menu
menubar.add_command(label="New job", command=None)
menubar.add_command(label="Load job", command=None)
root.config(menu=menubar)


def get_work_from_parameters():
    barrel = Barrel(diameter=barrel_diameter_var, height=barrel_height_var)
    template = Template(width=template_width_var, height=template_height_var, nb_copy=nb_copy_var)
    drill = Drill(diameter=drill_diameter_var)
    work = Work(barrel=barrel, template=template, drill=drill)

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

template_height_var = tk.DoubleVar()
template_height_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
template_height_entry = tk.Entry(root, textvariable=template_height_var, font=('calibre', 10, 'normal'))
template_height_label.grid(row=5, column=0)
template_height_entry.grid(row=5, column=1)

template_width_var = tk.DoubleVar()
width_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
width_entry = tk.Entry(root, textvariable=template_width_var, font=('calibre', 10, 'normal'))
width_label.grid(row=6, column=0)
width_entry.grid(row=6, column=1)

nb_copy_var = tk.IntVar()
nb_copy_label = tk.Label(root, text='Diameter', font=('calibre', 10, 'bold'))
nb_copy_entry = tk.Entry(root, textvariable=nb_copy_var, font=('calibre', 10, 'normal'))
nb_copy_label.grid(row=7, column=0)
nb_copy_entry.grid(row=7, column=1)

# Drill form 
drill_label = tk.Label(root, text='Drill', font=('calibre', 15, 'bold'))
drill_label.grid(row=8, column=0)

drill_diameter_var = tk.DoubleVar()
drill_diameter_label = tk.Label(root, text='drill_diameter', font=('calibre', 10, 'bold'))
drill_diameter_entry = tk.Entry(root, textvariable=drill_diameter_var, font=('calibre', 10, 'normal'))
drill_diameter_label.grid(row=9, column=0)
drill_diameter_entry.grid(row=9, column=1)


# Options
sub_btn = tk.Button(root, text='Start job', command=start_job)
save_btn = tk.Button(root, text='Save job', command=save_job)

sub_btn.grid(row=10, column=0)
save_btn.grid(row=10, column=1)

root.mainloop()
