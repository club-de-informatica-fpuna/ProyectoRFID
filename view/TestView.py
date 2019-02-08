from entidad.Carrera import Carrera
from entidad.Alumno import Alumno
from entidad.Socio import Socio
from datetime import datetime
from util.ConversorImg import ConversorImg

class TestView:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        self.generalController.carreraController.registrarCarrera(Carrera(denominacion="Lic. Hola"))
        self.generalController.carreraController.eliminarCarrera(23)
        self.generalController.carreraController.actualizarCarrera(Carrera(id=24, denominacion="Lic. m3 esta"))
        carreras = self.generalController.carreraController.listarCarreras()
        self.listarCarreras(carreras)
    
    def listarCarreras(self, carreras):
        for carrera in carreras:
            print(carrera)
    
    def initViewAlumnos(self):
        alumno = Alumno(ci="5416252", apellido=".|.", nombre=".|.", email="@gmail.com", telefono='051-516-151', idCarrera=1)
        #self.generalController.alumnoController.registrarAlumno(alumno)
        #self.generalController.alumnoController.eliminarAlumno("1234567")
        self.generalController.alumnoController.actualizarAlumnos(alumno)
        alumnos = self.generalController.alumnoController.listarAlumno()
        self.listarAlumnos(alumnos)

    def listarAlumnos(self, alumnos):
        for alumno in alumnos:
            print(alumno)

    def initSocio(self):
        #print(self.generalController.socioController.obtenerSocioCi(123456))
        #self.generalController.socioController.eliminarSocioCi(123456)
        #socio = Socio(4,4,123456, '/home/ivan/Descargas/icon-student-black.png', datetime.now(), False)
        #self.generalController.socioController.registrarSocio(socio)
        conversor = ConversorImg("/home/ivan/Descargas/images.png")
        base64foto = conversor.encodeImg()
        print(self.generalController.socioController.actualizarSocioCi(Socio(uid='5', foto=base64foto, estado=True, ci=123456)))
        #socios = self.generalController.socioController.listarSocios()
        #self.listarSocios(socios)
    
    def listarSocios(self, socios):
        for s in socios:
            print(s)