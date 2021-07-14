from model import Model
from view import View

from tkinter import filedialog
from utilities import load_sdrf, save_sdrf

class Controller():

    def __init__(self):
        self.model = Model()
        self.view = View(self.model)


        # Set the load button, loading sdrf file into the model
        self.view.load_sdrf_button.bind(
            "<Button-1>",  # <-- MouseButtonLeft
            lambda event: self.model.set_sdrf_struct(load_sdrf(self.set_sdrf_file()))
        )

        # Set the save button, saving the sdrf from model to disk
        self.view.save_sdrf_button.bind(
            "<Button-1>", # <-- MouseButtonLeft
            lambda event: save_sdrf(self.model.sdrf_struct, self.get_writable_sdrf_file())
        )


    def start(self):
        """ Start the View """
        self.view.master.mainloop()


    def set_sdrf_file(self):
        """ Open a file dialog requesting the sdrf to open """
        return filedialog.askopenfilename(filetypes=[("Table Seperated Values (SDRF)", ".tsv")])

    def get_writable_sdrf_file(self):
        """ Open a file dialog requesting the filename/loaction to save """
        return filedialog.asksaveasfilename(
            initialfile="sdrf.tsv", defaultextension=".tsv", filetypes=[("Table Seperated Values (SDRF)", ".tsv")]
        )
