from view.ejemplosPyQt.Login import Login
from view.ejemplosPyQt.SucursalSelect import SucursalSelect
from view.ejemplosPyQt.Home import Home
from PyQt5.QtWidgets import QApplication

class View:
    def __init__(self, generalController):
        self.generalController = generalController
    
    def iniciarVista(self):
        self.app = QApplication([])
        self.loginView = Login(self)
        self.loginView.iniciar()

    def mostrarInicio(self):
        self.homeView = Home(self)
        self.homeView.iniciar()