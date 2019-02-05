from view.View import View
from view.TestView import TestView
from model.Manager import Manager
from controller.CarreraController import CarreraController
from controller.AlumnoController import AlumnoController

class GeneralController:
    def __init__(self, exit):
        self.exit = exit
        self.manager = Manager(self)
        self.manager.iniciar()
        self.carreraController = CarreraController(self.manager.carreraManager)
        self.alumnoController = AlumnoController(self.manager.alumnoManager)
    
    def iniciarVista(self):
        vista = TestView(self)
        #vista.iniciarVista()
        vista.initViewAlumnos()