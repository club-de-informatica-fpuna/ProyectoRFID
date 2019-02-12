from view.contents.Home import Home
from view.contents.Alumnos import Alumnos
from view.contents.FormAlumno import FormAlumno
from PyQt5.QtWidgets import QApplication

class View:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.homeView = Home(self)
        self.homeView.start()
    
    def mostrarModuloAlumnos(self):
        self.alumnosView = Alumnos(self)
        self.alumnosView.start()

    def mostrarFormAlumno(self):
        self.formAlumno = FormAlumno(self)
        self.formAlumno.start() 
        