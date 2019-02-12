class CarreraController:

    def __init__(self, carreraManager):
        self.carreraManager = carreraManager

    def registrarCarrera(self, carrera):
        return self.carreraManager.registrarCarrera(carrera)
    
    def eliminarCarrera(self, idCarrera):
        return self.carreraManager.eliminarCarrera(idCarrera)
    
    def actualizarCarrera(self, carrera):
        return self.carreraManager.actualizarCarrera(carrera)
    
    def listarCarreras(self):
        return self.carreraManager.listarCarreras()
    
    def listarCarreraPorId(self, id):
        return self.carreraManager.listarCarrerasPorId(id)