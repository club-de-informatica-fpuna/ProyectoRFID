from view.View import View
from model.Manager import Manager

class GeneralController:
    def __init__(self, exit):
        self.exit = exit
        self.manager = Manager(self)
        self.manager.iniciar()
    
    def iniciarVista(self):
        vista = View(self)
        vista.iniciarVista()        

    
    