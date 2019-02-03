class CarreraController:

    def __init__(self, carreraManager):
        self.carreraManager = carreraManager

    def registrarCarrera(self, carrera):
        pass
    
    def eliminarCarrera(self, idCarrera):
        pass
    
    def actualizarCarrera(self, carrera):
        pass
    
    def listarCarreras(self):
        return self.carreraManager.listarCarreras()