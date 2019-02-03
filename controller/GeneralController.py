from view.View import View
from view.TestView import TestView
from model.Manager import Manager
from controller.CarreraController import CarreraController

class GeneralController:
    def __init__(self, exit):
        self.exit = exit
        self.manager = Manager(self)
        self.manager.iniciar()
        self.carreraController = CarreraController(self.manager.carreraManager)
    
    def iniciarVista(self):
        vista = TestView(self)
        vista.iniciarVista()