from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os

class Home:

    def __init__(self, view):
        self.view = view
        self.title = 'Inicio | CEP'
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon(os.getcwd()+'/view/resources/cep-logo.ico'))
        self.createGriLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()
        self.view.app.exec_()

    def createGriLayout(self):
        self.layout = QGridLayout()

        btnSocio = QPushButton('Socios')
        btnSocio.setObjectName('botonHome')
        btnSocio.clicked.connect(self.view.mostrarModuloSocio)

        btnAlumno = QPushButton('Alumnos')        
        btnAlumno.setObjectName('botonHome')
        btnAlumno.clicked.connect(self.view.mostrarModuloAlumnos)

        btnPrestamo = QPushButton('Prestamos')
        btnPrestamo.setObjectName('botonHome')
        btnVenta = QPushButton('Ventas')
        btnVenta.setObjectName('botonHome')
        btnPromocion = QPushButton('Promociones')
        btnPromocion.setObjectName('botonHome')
        btnCaja = QPushButton('Caja')
        btnCaja.setObjectName('botonHome')
        btnEquipo = QPushButton('Equipos')
        btnEquipo.setObjectName('botonHome')
        btnSalir = QPushButton('Salir')
        btnSalir.setObjectName('botonHome')
        btnSalir.clicked.connect(self.view.salir)
        labelTitle = QLabel('Sistema de Control del CEP')
        labelTitle.setObjectName('tituloHome')

        with open('./view/resources/styles.css') as f:
            labelTitle.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnSocio.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnAlumno.setStyleSheet(f.read())            
        with open('./view/resources/styles.css') as f:
            btnPrestamo.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnVenta.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnPromocion.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnCaja.setStyleSheet(f.read())                    
        with open('./view/resources/styles.css') as f:
            btnEquipo.setStyleSheet(f.read())                                
        with open('./view/resources/styles.css') as f:
            btnSalir.setStyleSheet(f.read())

        labelImg = QLabel()
        pixMap = QPixmap(os.getcwd()+'/view/resources/cep-logo.png')
        pixmap_resized = pixMap.scaled(100, 100, Qt.KeepAspectRatio)
        labelImg.setPixmap(pixmap_resized)
        labelImg.setStyleSheet('margin:auto')

        self.layout.addWidget(labelTitle, 0, 0, 1, 3)
        self.layout.addWidget(btnSocio, 1, 0)
        self.layout.addWidget(btnAlumno, 1, 2)
        self.layout.addWidget(btnPrestamo, 2, 0)
        self.layout.addWidget(btnVenta, 2, 2)
        self.layout.addWidget(btnPromocion, 3, 0)
        self.layout.addWidget(btnCaja, 3, 2)
        self.layout.addWidget(btnEquipo, 4, 0)
        self.layout.addWidget(btnSalir, 4, 2)
        self.layout.addWidget(labelImg, 1, 1, 4, 1)
        self.layout.setContentsMargins(50, 50, 50, 50)

        self.window.setObjectName("ventanaHome")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())        
        self.window.setLayout(self.layout)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.window.geometry()      
        self.window.move((screen.width() - size.width()) /2, (screen.height() - size.height()) / 2)
        self.window.setFixedSize(self.window.size())
