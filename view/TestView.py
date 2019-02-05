from entidad.Carrera import Carrera
from entidad.Alumno import Alumno
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
        alumno = Alumno(ci="1234567", apellido=".|.", nombre=".|.", email="@gmail.com", telefono='051-516-151', idCarrera=1)
        #self.generalController.alumnoController.registrarAlumno(alumno)
        self.generalController.alumnoController.eliminarAlumno("1234567")
        alumnos = self.generalController.alumnoController.listarAlumno()
        self.listarAlumnos(alumnos)

    def listarAlumnos(self, alumnos):
        for alumno in alumnos:
            print(alumno)
