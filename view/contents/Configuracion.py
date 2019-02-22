from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Configuracion:

    def __init__(self, view=None):
        self.view = view
        self.title = "Configuración | CEP"
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon("./view/resources/config.svg"))
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()

    def createGridLayout(self):
        pass
        
    def center(self):
        self.window.showMaximized()