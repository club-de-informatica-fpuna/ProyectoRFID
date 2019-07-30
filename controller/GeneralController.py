from view.View import View
from view.TestView import TestView
from model.Manager import Manager
from controller.CarreraController import CarreraController
from controller.AlumnoController import AlumnoController
from controller.SocioController import SocioController
from controller.PrestamosController import PrestamoController

class GeneralController:
    def __init__(self, exit):
        self.exit = exit
        self.manager = Manager(self)
        self.manager.iniciar()
        self.carreraController = CarreraController(self.manager.carreraManager)
        self.alumnoController  = AlumnoController(self.manager.alumnoManager)
        self.socioController   = SocioController(self.manager.socioManager)
        self.prestamoController = PrestamoController(self.manager.prestamoManager)
    
    def iniciarVista(self):
        vista = View(self)
        #vista.iniciarVista()
        #vista.initViewAlumnos()
        vista.iniciarVista()
