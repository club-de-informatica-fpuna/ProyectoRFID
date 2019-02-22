from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os

class Popup:

    def __init__(self, view=None, titleWindow="", title="", message=""):
        self.view = view
        self.titleWindow = titleWindow
        self.title = title
        self.message = message
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.titleWindow)
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QVBoxLayout(self.window)

        labelTitulo = QLabel(self.title)
        labelTitulo.setObjectName("tituloPopup")

        labelMessage = QLabel("")

        messages = []

        if type(self.message) == list:
            for i in self.message:
                qlabel = QLabel(i)
                qlabel.setObjectName("tituloMensaje")
                with open('./view/resources/styles.css') as f:
                    qlabel.setStyleSheet(f.read())
                messages.append(qlabel)
        else:
            labelMessage = QLabel(self.message)
            labelMessage.setObjectName("tituloMensaje")

        btnCerrar = QPushButton("Cerrar")
        btnCerrar.setObjectName("botonPrimario")        
        btnCerrar.clicked.connect(self.manejarCancelar)
        btnCerrar.setContentsMargins(0,20,0,0)

        with open('./view/resources/styles.css') as f:
            labelTitulo.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            labelMessage.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnCerrar.setStyleSheet(f.read())                                

        self.layout.addWidget(labelTitulo)
        if type(self.message) == list:
            for i in messages:
                self.layout.addWidget(i)
        else:
            self.layout.addWidget(labelMessage)            
        self.layout.addWidget(btnCerrar)        
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.window.setObjectName("ventanaPopup")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())

        shortcutCerrar = QShortcut(QKeySequence(Qt.Key_Return), btnCerrar)
        shortcutCerrar.setContext(Qt.WidgetShortcut)
        shortcutCerrar.activated.connect(self.window.hide)              

    def center(self):
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
        
    def manejarCancelar(self):
        self.window.hide()