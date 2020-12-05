import tkinter as tk

from ihm.work_config_frame import WorkConfigFrame
from ihm.work_image_frame import WorkImageFrame

from controllers import work_manager


class MainFrame(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("First_Program")
        self.attributes('-fullscreen', 1)

        self.current_frame = WorkConfigFrame(self)

    def display_form_frame(self):
        self.current_frame.destroy()
        self.current_frame = WorkConfigFrame(self)
        if work_manager.current_work:
            self.current_frame.set_form_data(work_manager.current_work)

    def display_image_frame(self):
        self.current_frame.destroy()
        self.current_frame = WorkImageFrame(self)
        work_manager.generate_matrix_thread(self.current_frame.display_matrix_preview)


MainFrame().mainloop()
