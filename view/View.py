from view.contents.Home import Home
from view.contents.Alumnos import Alumnos
from view.contents.FormAlumno import FormAlumno
from view.contents.FormSocios import FormSocios
from view.contents.Socios import Socio
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
    
    def mostrarFormSocio(self):
        self.formSocio = FormSocios(self)
        self.formSocio.start()
    
    def mostrarModuloSocio(self):
        self.socioView = Socio(self)
        self.socioView.start()
    
    def salir(self):
        self.app.exit()