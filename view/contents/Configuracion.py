from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.contents.Carreras import Carreras
from view.contents.BaseDatos import BaseDatos

class Configuracion:

    def __init__(self, view=None):
        self.view = view
        self.title = "Configuración | CEP"
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon("./view/resources/config.svg"))
        self.createLayout()
        self.center()

    def createLayout(self):
        self.layout = QVBoxLayout(self.window)
        self.tabsView = QTabWidget()
        carrerasWidget = Carreras(self.view)
        baseDatosWidget = BaseDatos(self.view)
        self.tabCarreras = carrerasWidget.getWidgetBuilded()
        self.tabBaseDatos = baseDatosWidget.getWidgetBuilded()
        self.tabsView.addTab(self.tabCarreras, "Carreras")
        self.tabsView.addTab(self.tabBaseDatos, "Base de datos")
        self.layout.addWidget(self.tabsView)

    def start(self):
        self.build()

    def center(self):
        self.window.showMaximized()