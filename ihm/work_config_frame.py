import tkinter as tk
import tkinter.ttk

from ihm.keyboard import Keyboard

from objects.work import Work
from objects.drill import Drill
from objects.barrel import Barrel
from objects.template import Template
from objects.margin import Margin
from controllers import work_manager, save_manager

form_grid_pady = 10


class WorkConfigFrame(tk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Container frame
        self.pack(expand=True)

        # Popup keyboard
        self.keyboard = None

        # Form frame
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0)

        # Separator
        tkinter.ttk.Separator(self, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=50)

        # Save frame
        self.save_frame = tk.Frame(self)
        self.save_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=50, pady=10)

        # Barrel form
        barrel_frame = tk.Frame(self.form_frame)
        barrel_frame.grid(row=0, column=0, pady=form_grid_pady)

        barrel_label = tk.Label(barrel_frame, text='Fut', font=('calibre', 15, 'bold'))
        barrel_label.grid(row=0, column=0)

        self.barrel_diameter_var = tk.DoubleVar()
        barrel_diameter_label = tk.Label(barrel_frame, text='Diamètre', font=('calibre', 10, 'bold'))
        barrel_diameter_entry = tk.Entry(barrel_frame, textvariable=self.barrel_diameter_var, font=('calibre', 10, 'normal'))
        barrel_diameter_units_label = tk.Label(barrel_frame, text='mm', font=('calibre', 10))
        barrel_diameter_label.grid(row=1, column=0, padx=10)
        barrel_diameter_entry.grid(row=1, column=1)
        barrel_diameter_units_label.grid(row=1, column=2)

        self.barrel_height_var = tk.DoubleVar()
        barrel_height_label = tk.Label(barrel_frame, text='Hauteur', font=('calibre', 10, 'bold'))
        barrel_height_entry = tk.Entry(barrel_frame, textvariable=self.barrel_height_var, font=('calibre', 10, 'normal'))
        barrel_height_units_label = tk.Label(barrel_frame, text='mm', font=('calibre', 10))
        barrel_height_label.grid(row=2, column=0, padx=10)
        barrel_height_entry.grid(row=2, column=1)
        barrel_height_units_label.grid(row=2, column=2)

        # Motif form
        motif_frame = tk.Frame(self.form_frame)
        motif_frame.grid(row=1, column=0, pady=form_grid_pady)

        motif_label = tk.Label(motif_frame, text='Motif', font=('calibre', 15, 'bold'))
        motif_label.grid(row=0, column=0)

        self.template_height_var = tk.DoubleVar()
        template_height_label = tk.Label(motif_frame, text='Hauteur', font=('calibre', 10, 'bold'))
        template_height_entry = tk.Entry(motif_frame, textvariable=self.template_height_var, font=('calibre', 10, 'normal'))
        template_height_units_label = tk.Label(motif_frame, text='mm', font=('calibre', 10))
        template_height_label.grid(row=1, column=0, padx=10)
        template_height_entry.grid(row=1, column=1)
        template_height_units_label.grid(row=1, column=2)

        self.template_width_var = tk.DoubleVar()
        template_width_label = tk.Label(motif_frame, text='Largeur', font=('calibre', 10, 'bold'))
        template_width_entry = tk.Entry(motif_frame, textvariable=self.template_width_var, font=('calibre', 10, 'normal'))
        template_width_units_label = tk.Label(motif_frame, text='mm', font=('calibre', 10))
        template_width_label.grid(row=2, column=0, padx=10)
        template_width_entry.grid(row=2, column=1)
        template_width_units_label.grid(row=2, column=2)

        self.nb_copy_var = tk.IntVar()
        nb_copy_label = tk.Label(motif_frame, text='Iterations', font=('calibre', 10, 'bold'))
        nb_copy_entry = tk.Entry(motif_frame, textvariable=self.nb_copy_var, font=('calibre', 10, 'normal'))
        nb_copy_label.grid(row=3, column=0, padx=10)
        nb_copy_entry.grid(row=3, column=1)

        # Drill form
        drill_frame = tk.Frame(self.form_frame)
        drill_frame.grid(row=2, column=0, pady=form_grid_pady)

        drill_label = tk.Label(drill_frame, text='Fraiseuse', font=('calibre', 15, 'bold'))
        drill_label.grid(row=0, column=0)

        self.drill_diameter_var = tk.DoubleVar()
        drill_diameter_label = tk.Label(drill_frame, text='Diamètre', font=('calibre', 10, 'bold'))
        drill_diameter_entry = tk.Entry(drill_frame, textvariable=self.drill_diameter_var, font=('calibre', 10, 'normal'))
        drill_diameter_units_label = tk.Label(drill_frame, text='mm', font=('calibre', 10))
        drill_diameter_label.grid(row=1, column=0, padx=10)
        drill_diameter_entry.grid(row=1, column=1)
        drill_diameter_units_label.grid(row=1, column=2)

        # Margin form
        margin_frame = tk.Frame(self.form_frame)
        margin_frame.grid(row=4, column=0, pady=form_grid_pady)

        drill_label = tk.Label(margin_frame, text='Marge', font=('calibre', 15, 'bold'))
        drill_label.grid(row=0, column=0)

        self.margin_x = tk.DoubleVar()
        margin_x_label = tk.Label(margin_frame, text='Marge X', font=('calibre', 10, 'bold'))
        margin_x_entry = tk.Entry(margin_frame, textvariable=self.margin_x, font=('calibre', 10, 'normal'))
        margin_x_unit_label = tk.Label(margin_frame, text='mm', font=('calibre', 10))
        margin_x_label.grid(row=1, column=0, padx=10)
        margin_x_entry.grid(row=1, column=1)
        margin_x_unit_label.grid(row=1, column=2)

        self.margin_y = tk.DoubleVar()
        margin_y_label = tk.Label(margin_frame, text='Marge y', font=('calibre', 10, 'bold'))
        margin_y_entry = tk.Entry(margin_frame, textvariable=self.margin_y,
                                  font=('calibre', 10, 'normal'))
        margin_y_unit_label = tk.Label(margin_frame, text='mm', font=('calibre', 10))
        margin_y_label.grid(row=2, column=0, padx=10)
        margin_y_entry.grid(row=2, column=1)
        margin_y_unit_label.grid(row=2, column=2)
        # Options
        self.save_name = tk.StringVar()
        preview_btn = tk.Button(self.form_frame, text='Valider', command=self.preview,  height = 5, width = 10)

        preview_btn.grid(row=6, column=0, pady=form_grid_pady)

        # Save Frame
        self.label = tk.Label(self.save_frame, text="Paramètres sauvegardés", font=('calibre', 15, 'bold'))
        self.label.pack(side=tk.TOP, anchor="w")

        self.listbox = tk.Listbox(self.save_frame, width=400, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=20)
        scrollbar = tk.Scrollbar(self.listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.load_work_params)

        save_manager.load_saves()
        for save_name in save_manager.saves.keys():
            self.listbox.insert(tk.END, save_name)

        self.save_name_entry = tk.Entry(self.save_frame, textvariable=self.save_name, font=('calibre', 10, 'normal'))
        self.save_name_entry.bind('<FocusIn>', self.display_keyboard)
        self.save_name_entry.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.save_frame, text='Supprimer sauvegarde', command=self.delete_work,height=5, width=15, wraplength=80)
        self.delete_button.pack(side=tk.RIGHT)

        self.save_button = tk.Button(self.save_frame, text='Nouvelle sauvegarde', command=self.save_work,height=5, width=15, wraplength=80)
        self.save_button.pack(side=tk.RIGHT)

    def keyboard_destroyed(self, event):
        self.focus()
        self.keyboard = None

    def display_keyboard(self, event):
        if self.keyboard:
            self.keyboard.quit()
        self.keyboard = Keyboard(event.widget)
        self.keyboard.bind('<Destroy>', self.keyboard_destroyed)
        self.keyboard.mainloop()

    def load_work_params(self, val):

        save_name = str(self.listbox.get(tk.ANCHOR))

        work = save_manager.saves[save_name]

        self.set_form_data(work)

    def get_work_from_parameters(self):

        # Create Work instance from form values
        barrel = Barrel(diameter=self.barrel_diameter_var.get(), height=self.barrel_height_var.get())
        template = Template(width=self.template_width_var.get(), height=self.template_height_var.get(), nb_copy=self.nb_copy_var.get())
        drill = Drill(diameter=self.drill_diameter_var.get())
        margin = Margin(margin_x=self.margin_x.get(), margin_y=self.margin_y.get())

        work = Work(barrel=barrel, template=template, drill=drill, margin=margin)

        return work

    def set_form_data(self, work):

        # Set form values from work
        self.barrel_diameter_var.set(work.barrel.diameter)
        self.barrel_height_var.set(work.barrel.height)

        self.template_width_var.set(work.template.width)
        self.template_height_var.set(work.template.height)
        self.nb_copy_var.set(work.template.nb_copy)

        self.drill_diameter_var.set(work.drill.diameter)
        self.margin_x.set(work.margin.margin_x)
        self.margin_y.set(work.margin.margin_y)

    def preview(self):
        work_manager.current_work = self.get_work_from_parameters()
        validated, message = work_manager.current_work.validate()
        if not validated:
            self.pop_up_error(message)
        else:
            self.display_work_image()

    def save_work(self):
        if not self.save_name.get() or self.save_name.get() in save_manager.saves.keys():
            return
        if self.keyboard:
            self.keyboard.quit()
        work_manager.current_work = self.get_work_from_parameters()
        save_manager.save_work(self.save_name.get(), work_manager.current_work)
        self.listbox.insert(tk.END, self.save_name.get())
        self.save_name_entry.delete(0, 'end')

    def delete_work(self):

        save_name = str(self.listbox.get(tk.ANCHOR))

        save_manager.delete_save(save_name)
        self.listbox.delete(tk.ANCHOR)

    def display_work_image(self):
        self.master.display_image_frame()

    def pop_up_error(self, text_message):
        f_infos = tk.Toplevel()  # Popup -> Toplevel()
        f_infos.title("Erreur lors des contrôles")
        tk.Label(f_infos,text=text_message, font=('calibre', 20, 'bold')).pack()
        tk.Button(f_infos, text='Quitter', command=f_infos.destroy).pack(padx=20, pady=20)
        f_infos.transient(self.master)  # Réduction popup impossible
        f_infos.grab_set()  # Interaction avec fenetre jeu impossible
        self.master.wait_window(f_infos)
