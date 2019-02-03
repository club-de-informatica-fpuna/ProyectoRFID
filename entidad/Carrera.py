class Carrera:

    def __init__(self, id=None, denominacion=None):
        self.id = id
        self.denominacion = denominacion
    
    def __str__(self):
        return str(self.id) + ": " + str(self.denominacion)
