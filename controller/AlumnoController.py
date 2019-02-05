class AlumnoController:

    def __init__(self, alumnoManager):
        self.alumnoManager = alumnoManager
    
    def listarAlumno(self):
        return self.alumnoManager.listarAlumno()
    
    def registrarAlumno(self, alumno):
        return self.alumnoManager.registrarAlumno(alumno)

    def eliminarAlumno(self, idSpanner):
        return self.alumnoManager.eliminarAlumno(idSpanner)