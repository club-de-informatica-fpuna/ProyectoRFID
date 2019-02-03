class TestView:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        carreras = self.generalController.carreraController.listarCarreras()
        self.listarCarreras(carreras)
    
    def listarCarreras(self, carreras):
        for carrera in carreras:
            print(carrera)