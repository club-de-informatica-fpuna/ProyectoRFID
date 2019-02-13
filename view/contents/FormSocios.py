from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class FormSocios:

    def __init__(self, view):
        self.view = view
        self.title = 'Nuevo Socio | CEP'

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.createGridLayout()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)
        horizontalLayout = QHBoxLayout()

        labelTitle = QLabel('Registrar Alumno')

        ci        = QLabel("C.I.")
        firstName = QLabel("Nombres")
        lastName  = QLabel("Apellidos")
        eMail     = QLabel("E-mail")
        phone     = QLabel("Telefono")
        career    = QLabel("Carrera")

        self.inputCI     = QLineEdit()
        self.inputFN     = QLineEdit()
        self.inputLN     = QLineEdit()
        self.inputEM     = QLineEdit()
        self.inputPhone  = QLineEdit()
        self.inputCarrer = QComboBox()

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setObjectName("botonPrimario")

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("botonPrimario")        

        with open('./view/resources/styles.css') as f:
            btnCancelar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnRegistrar.setStyleSheet(f.read())

        horizontalLayout.addWidget(btnRegistrar)
        horizontalLayout.addWidget(btnCancelar)
        self.layout.addLayout(horizontalLayout,0,0)

        

