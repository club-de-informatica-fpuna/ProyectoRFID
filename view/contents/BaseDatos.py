from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class BaseDatos:

    def __init__(self, view):
        self.view = view
        #self.carreras = self.view.generalController.carreraController.listarCarreras()

    def constriur(self):
        self.widget = QWidget()
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget