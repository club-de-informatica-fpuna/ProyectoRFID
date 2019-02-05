from entidad.Carrera import Carrera
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