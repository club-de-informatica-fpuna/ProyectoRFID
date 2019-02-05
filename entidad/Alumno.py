class Alumno:

    def __init__(self, ci=None, apellido='', nombre='', email='', telefono='',idCarrera=None ):
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.idCarrera = idCarrera
    
    def __str__(self):
        return ("\tALUMNO\nC.I.: "+str(self.ci)+"\nNombre: " + str(self.nombre)+"\nApellido: "+str(self.apellido)+"\nE-mail: "+str(self.email)+ "\nTelefono: "+str(self.telefono)+"\nInf. Carrera: "+str(self.idCarrera)+"\n")