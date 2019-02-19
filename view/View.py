from view.contents.Home import Home
from view.contents.Popup import Popup
from view.contents.Alumnos import Alumnos
from view.contents.FormAlumno import FormAlumno
from view.contents.FormSocios import FormSocios
from view.contents.Socios import Socio
from view.contents.ConsultaSocio import ConsultaSocio
from view.contents.Webcam import Webcam
from PyQt5.QtWidgets import QApplication
import math

class View:
    def __init__(self, generalController):
        self.generalController = generalController
        self.alumnosView = None
        self.socioView   = None
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.homeView = Home(self)
        self.homeView.start()
    
    def mostrarModuloAlumnos(self):
        if self.alumnosView is not None:
            cantidadAlumnos = self.alumnosView.cantidadAlumnos
            if cantidadAlumnos is None or cantidadAlumnos <= 0:
                self.alumnosView = Alumnos(self)
            else:
                cantPaginas = math.ceil(cantidadAlumnos/self.alumnosView.cantidadElementos)
                self.alumnosView = Alumnos(self, cantPaginas)
        else:
            self.alumnosView = Alumnos(self)            
        self.alumnosView.start()

    def mostrarFormAlumno(self, title="Nuevo alumno | CEP", update=False, alumnoUpdate=None, editable=True):
        if title is False:
            title = "Nuevo alumno | CEP"
        self.formAlumno = FormAlumno(self, title=title, update=update, alumnoUpdate=alumnoUpdate, editable=editable)
        self.formAlumno.start()        
    
    def mostrarFormSocio(self, title='', update=False, socio=None):
        if update:
            self.formSocio = FormSocios(self,title=title, update=update, socio=socio)
        else:
            self.formSocio = FormSocios(self, title="Nuevo Socio | CEP", update=update, socio=socio)

        self.formSocio.start()
    
    def mostrarModuloSocio(self):
        if self.socioView is not None:
            quantityPartner = self.socioView.totalPartner
            if quantityPartner <= 0 :
                self.socioView = Socio(self)
            else:
                amountOfPage = math.ceil(quantityPartner/self.socioView.totalPartner)
                self.socioView = Socio(self, amountOfPage)
        else:
            self.socioView = Socio(self)
        self.socioView.start()

    def mostrarConsultaSocio(self, socio, alumno, carrera):
        self.consultaSocio = ConsultaSocio(socio, alumno, carrera)
        self.consultaSocio.start()
    
    def salir(self):
        self.app.exit()

    def mostrarPopup(self, titleWindow, title, message):
        self.popup = Popup(view=self, title=title, titleWindow=titleWindow, message=message)
        self.popup.start()
    
    def mostrarWebcam(self, filename, setPhoto):
        self.webcamView = Webcam(filename, setPhoto)
        self.webcamView.start()