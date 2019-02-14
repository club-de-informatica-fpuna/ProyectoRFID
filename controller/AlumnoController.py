class AlumnoController:

    def __init__(self, alumnoManager):
        self.alumnoManager = alumnoManager
    
    def listarAlumno(self):
        return self.alumnoManager.listarAlumno()
    
    def registrarAlumno(self, alumno):
        return self.alumnoManager.registrarAlumno(alumno)

    def eliminarAlumno(self, idSpanner):
        return self.alumnoManager.eliminarAlumno(idSpanner)

    def actualizarAlumnos(self, alumno):
        return self.alumnoManager.actualizarAlumnos(alumno)

    def listarAlumnoPaginado(self, pagina, cantElementos):
        return self.alumnoManager.listarAlumnoPaginado(pagina, cantElementos)

    def getCantidadAlumnos(self):
        return self.alumnoManager.getCantidadAlumnos()
    
    def buscarAlumno(self, ci):
        return self.alumnoManager.buscarAlumno(ci)