class Prestamo:

    def __init__(self, descripcion='', nombre='',apellido='', ci=None, telefono=None, denominacion='',fecha_prestamo='',fecha_devolucion='',estado=None):
        self.descripcion=descripcion
        self.nombre = nombre
        self.apellido=apellido
        self.ci = ci
        self.telefono = telefono
        self.denominacion=denominacion
        self.fecha_prestamo=fecha_prestamo
        self.fecha_devolucion=fecha_devolucion
        self.estado = estado

    def __str__(self):
        return ("\tPRÉSTAMO\nEquipo: "+str(self.descripcion)+"\nNombre:"+(str(self.nombre))+"\nApellido:"+(str(self.apellido))+"\nC.I.: "+str(self.ci)+"\nTeléfono: "+str(self.telefono)+"\nCarrera: "+str(self.denominacion)+"\nFecha Prestamo: "+str(self.fecha_prestamo)+ "\nFecha Devolucion: "+str(self.fecha_devolucion)+"\nEstado: "+str(self.estado)+"\n")