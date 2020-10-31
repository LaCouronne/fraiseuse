import tkinter as tk

from objects.work import Work
from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template

form_grid_pady = 10


class WorkConfigFrame(tk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Work config frame
        self.place(x=30, y=30)

        # Barrel form
        barrel_frame = tk.Frame(self)
        barrel_frame.grid(row=0, column=0, pady=form_grid_pady)

        barrel_label = tk.Label(barrel_frame, text='Barrel', font=('calibre', 15, 'bold'))
        barrel_label.grid(row=0, column=0)

        self.barrel_diameter_var = tk.DoubleVar()
        barrel_diameter_label = tk.Label(barrel_frame, text='Diameter', font=('calibre', 10, 'bold'))
        barrel_diameter_entry = tk.Entry(barrel_frame, textvariable=self.barrel_diameter_var, font=('calibre', 10, 'normal'))
        barrel_diameter_units_label = tk.Label(barrel_frame, text='mm', font=('calibre', 10))
        barrel_diameter_label.grid(row=1, column=0)
        barrel_diameter_entry.grid(row=1, column=1)
        barrel_diameter_units_label.grid(row=1, column=2)

        self.barrel_height_var = tk.DoubleVar()
        barrel_height_label = tk.Label(barrel_frame, text='Height', font=('calibre', 10, 'bold'))
        barrel_height_entry = tk.Entry(barrel_frame, textvariable=self.barrel_height_var, font=('calibre', 10, 'normal'))
        barrel_height_units_label = tk.Label(barrel_frame, text='mm', font=('calibre', 10))
        barrel_height_label.grid(row=2, column=0)
        barrel_height_entry.grid(row=2, column=1)
        barrel_height_units_label.grid(row=2, column=2)

        # Motif form
        motif_frame = tk.Frame(self)
        motif_frame.grid(row=1, column=0, pady=form_grid_pady)

        motif_label = tk.Label(motif_frame, text='Motif', font=('calibre', 15, 'bold'))
        motif_label.grid(row=0, column=0)

        self.template_height_var = tk.DoubleVar()
        template_height_label = tk.Label(motif_frame, text='Height', font=('calibre', 10, 'bold'))
        template_height_entry = tk.Entry(motif_frame, textvariable=self.template_height_var, font=('calibre', 10, 'normal'))
        template_height_units_label = tk.Label(motif_frame, text='mm', font=('calibre', 10))
        template_height_label.grid(row=1, column=0)
        template_height_entry.grid(row=1, column=1)
        template_height_units_label.grid(row=1, column=2)

        self.template_width_var = tk.DoubleVar()
        template_width_label = tk.Label(motif_frame, text='Width', font=('calibre', 10, 'bold'))
        template_width_entry = tk.Entry(motif_frame, textvariable=self.template_width_var, font=('calibre', 10, 'normal'))
        template_width_units_label = tk.Label(motif_frame, text='mm', font=('calibre', 10))
        template_width_label.grid(row=2, column=0)
        template_width_entry.grid(row=2, column=1)
        template_width_units_label.grid(row=2, column=2)

        self.nb_copy_var = tk.IntVar()
        nb_copy_label = tk.Label(motif_frame, text='Iterations', font=('calibre', 10, 'bold'))
        nb_copy_entry = tk.Entry(motif_frame, textvariable=self.nb_copy_var, font=('calibre', 10, 'normal'))
        nb_copy_label.grid(row=3, column=0)
        nb_copy_entry.grid(row=3, column=1)

        # Drill form
        drill_frame = tk.Frame(self)
        drill_frame.grid(row=2, column=0, pady=form_grid_pady)

        drill_label = tk.Label(drill_frame, text='Drill', font=('calibre', 15, 'bold'))
        drill_label.grid(row=0, column=0)

        self.drill_diameter_var = tk.DoubleVar()
        drill_diameter_label = tk.Label(drill_frame, text='Diameter', font=('calibre', 10, 'bold'))
        drill_diameter_entry = tk.Entry(drill_frame, textvariable=self.drill_diameter_var, font=('calibre', 10, 'normal'))
        drill_diameter_units_label = tk.Label(drill_frame, text='mm', font=('calibre', 10))
        drill_diameter_label.grid(row=1, column=0)
        drill_diameter_entry.grid(row=1, column=1)
        drill_diameter_units_label.grid(row=1, column=2)

        # Options
        sub_btn = tk.Button(self, text='Start job', command=self.start_work)
        save_btn = tk.Button(self, text='Save job', command=self.save_work)

        sub_btn.grid(row=3, column=0, pady=form_grid_pady)
        save_btn.grid(row=3, column=1, pady=form_grid_pady)

    def get_work_from_parameters(self):
        barrel = Barrel(diameter=self.barrel_diameter_var.get(), height=self.barrel_height_var.get())
        template = Template(width=self.template_width_var.get(), height=self.template_height_var.get(), nb_copy=self.nb_copy_var.get())
        drill = Drill(diameter=self.drill_diameter_var.get())
        work = Work(barrel=barrel, template=template, drill=drill)
        return work

    def start_work(self):
        work = self.get_work_from_parameters()
        validated, message = work.validate()
        if not validated:
            self.pop_up_error(message)
        else:
            self.pop_up_validation(work)

    def save_work(self):
        pass

    def pop_up_validation(self, work):
        f_infos = tk.Toplevel()  # Popup -> Toplevel()
        f_infos.title(str(work.drill.diameter))
        tk.Button(f_infos, text='Quitter', command=f_infos.destroy).pack(padx=10, pady=10)
        f_infos.transient(self.master)  # Réduction popup impossible
        f_infos.grab_set()  # Interaction avec fenetre jeu impossible
        self.master.wait_window(f_infos)

    def pop_up_error(self, text_message):
        f_infos = tk.Toplevel()  # Popup -> Toplevel()
        f_infos.title(text_message)
        tk.Button(f_infos, text='Quitter', command=f_infos.destroy).pack(padx=10, pady=10)
        f_infos.transient(self.master)  # Réduction popup impossible
        f_infos.grab_set()  # Interaction avec fenetre jeu impossible
        self.master.wait_window(f_infos)
