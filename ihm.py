import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
import os
import tinydb
import instructionCreations
import dao
from WorkManager import WorkManager

work_manager = WorkManager()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen', 1)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.current_selected = None
        self.frames = {}
        # Liste des pages disponibles
        for F in (
                HomePage, RecentsPage, ParamsPage, AdminPage, ValidationPage, ProcessingPage, ErrorProcessPage,
                EndProcessPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def edit_current_selection(selected):
        print("lancé"+ selected)
        SampleApp.current_selected=selected

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    # Cette fonction permet d'ouvrir une nouvelle fenetre avec des parametres
    def show_frame_arg(self, page_name,arg):
        frame = self.frames[page_name]
        if arg:
            frame.arg = arg
        frame.tkraise()

# home -> (motifs recents, parametres, admin) (HomePage)


class HomePage(tk.Frame):

    def helloCallBack(self):
        # os.system('control.py')
        instructionCreations.a.tableau()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bonjour ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Parametres récents",
                            command=lambda: controller.show_frame("RecentsPage"))
        button2 = tk.Button(self, text="Nouveaux parametres ",
                            command=lambda: controller.show_frame("ParamsPage"))
        button3 = tk.Button(self, text="Parametres administrateur",
                            command=lambda: controller.show_frame("AdminPage"))
        button4 = tk.Button(self, text="Parametres administrateur",
                            command=self.helloCallBack)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


# motifs recents -> (validation + datas, home) (RecentsPage)

class RecentsPage(tk.Frame):

    def validation_selected_parameter(self,listbox_barrel,listbox_template):
        pass

    def __init__(self, parent, controller):
        print()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Parametres recents", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        lb1 = tk.Listbox(self)
        list_barrel = dao.get_all_parameter_barrel()

        for i in list_barrel:
            lb1.insert("end", i)
#        lb1.get(lb1.curselection())



        listbox_template = tk.Listbox(self)
        list_template = dao.get_all_parameter_template()
        for template in list_template:
            listbox_template.insert("end",template)
#        listbox_template.get(listbox_template.curselection())

        validationButton = tk.Button(self, text="Valider les parametres",
                                     command=lambda: [
                                                      self.controller.show_frame("ValidationPage"),
                                                                                     self.validation_selected_parameter(lb1.get(lb1.curselection()),
                                                                                                                        listbox_template.get(listbox_template.curselection()))])
        homeButton = tk.Button(self, text="Go to the start page",
                               command=lambda: controller.show_frame("HomePage"))
        lb1.pack()
        listbox_template.pack()
        validationButton.pack()
        homeButton.pack()


# Parametres -> (validation + datas, home) (ParamsPage)


class ParamsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Entrer les parametres de la nouvelle emprunte", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        entries = {}
        for field in work_manager.work_fields:
                    lab = tk.Label(self, width=22, text=field + ": ")
                    ent = tk.Entry(self)
                    #ent.insert(0, "0")
                    lab.pack()
                    ent.pack()
                    entries[field] = ent

        validationButton = tk.Button(self, text="Valider les parametres",
                                     command=lambda: ParamsPage.save_parameters_and_go(self,entries,controller))
        homeButton = tk.Button(self, text="Retour menu",
                               command=lambda: controller.show_frame("HomePage"))
        validationButton.pack(side="bottom")
        homeButton.pack()

    def save_parameters_and_go(self,entries,controller):
        print(entries.)
        controller.show_frame("ValidationPage")


# Administrateur -> Home (AdminPage)

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Parametres administrateur: \n Taille fraiseuse: \n ...",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Valider et retour au menu ",
                            command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Ne pas enregistrer",
                            command=lambda: controller.show_frame("HomePage"))
        button1.pack()
        button2.pack()


# Validation form -> (process, home) (ValidationPage)
class ValidationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        args=" - "
        label = tk.Label(self, text="Validation en cours", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        print("caca")
#        print(SampleApp.current_selected)
#        label2 = tk.Label(self, text=str(SampleApp.current_selected))
        button1 = tk.Button(self, text="Lancer l'impression",
                            command=lambda: controller.show_frame("ProcessingPage"))
        button2 = tk.Button(self, text="Erreur, retour au menu",
                            command=lambda: controller.show_frame("HomePage"))

        label.pack()
       # label2.pack()
        button1.pack()
        button2.pack()
        print("end validation page")


# Process -> (end process, error) (PrecessingPage)
class ProcessingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Arret machine: Erreur ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Une erreur s'est produite",
                            command=lambda: controller.show_frame("ErrorProcessingPage"))
        button2 = tk.Button(self, text="Fin de process",
                            command=lambda: controller.show_frame("EndProcessPage"))
        button1.pack()
        button2.pack()


# Error -> a definir  (ErrorProcessPage)
class ErrorProcessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Impression de l'emprunte en cours", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Une erreur s'est produite",
                            command=lambda: controller.show_frame("Retour au menu"))

        button1.pack()


# EndProcessPage -> homepage (ErrorProcessPage)
class EndProcessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="L'impression s'est bien passée. ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Retour au menu",
                            command=lambda: controller.show_frame("HomePage"))

        button1.pack()


'''class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom
'''


def launch_ihm():
    app = SampleApp()
    app.mainloop()
    root = tk.Tk()
    # app = FullScreenApp(root)
    app.mainloop()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    root = tk.Tk()
    # app = FullScreenApp(root)
    root.mainloop()
