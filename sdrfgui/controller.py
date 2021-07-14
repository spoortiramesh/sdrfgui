from model import Model
from view import View

class Controller():

    def __init__(self):
        self.model = Model()
        self.view = View(self.model)


    def start(self):
        self.view.master.mainloop()
