from view.contents.Home import Home
from view.contents.Popup import Popup
from view.contents.Alumnos import Alumnos
from view.contents.Prestamos import Prestamos
from view.contents.FormAlumno import FormAlumno
from view.contents.FormSocios import FormSocios
from view.contents.FormPrestamo import FormPrestamo
from view.contents.Socios import Socio
from view.contents.ConsultaSocio import ConsultaSocio
from view.contents.Configuracion import Configuracion
from view.contents.Webcam import Webcam
from PyQt5.QtWidgets import QApplication
import math

class View:
    def __init__(self, generalController):
        self.generalController = generalController
        self.alumnosView = None
        self.socioView   = None
        self.prestamosView = None
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.homeView = Home(self)
        self.homeView.start()
    
    def mostrarModuloPrestamo(self):
        if self.prestamosView is not None:
            cantidadPrestamos = self.prestamosView.cantidadPrestamos
            if cantidadPrestamos is None or cantidadPrestamos <= 0:
                self.prestamosView = Prestamos(self)
            else:
                cantPaginas = math.ceil(cantidadPrestamos/self.prestamosView.cantidadElementos)
                self.prestamosView = Prestamos(self, cantPaginas)
        else:
            self.prestamosView = Prestamos(self)            
        self.prestamosView.start()

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

    def mostrarFormAlumno(self, title="Nuevo alumno | CEP", update=False, alumnoUpdate=None, editable=True, raceById=None):
        if title is False:
            title = "Nuevo alumno | CEP"
        self.formAlumno = FormAlumno(self, title=title, update=update, alumnoUpdate=alumnoUpdate, editable=editable, raceById=raceById)
        self.formAlumno.start()        

    def mostrarFormPrestamo(self, title="Nuevo préstamo | CEP", update=False, alumnoUpdate=None, editable=True, raceById=None):
        if title is False:
            title = "Nuevo préstamo | CEP"
        self.formPrestamo = FormPrestamo(self, title=title, update=update, prestamo=prestamo, editable=editable, raceById=raceById)
        self.formPrestamo.start()        
    
    def mostrarFormSocio(self, title='', update=False, socio=None, alumno=None, carrera=None):
        if update:
            self.formSocio = FormSocios(self,title=title, update=update, socio=socio, alumno=alumno, carrera=carrera)
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
    
    def mostrarConfiguracion(self):
        self.configView = Configuracion(self)
        self.configView.start()
