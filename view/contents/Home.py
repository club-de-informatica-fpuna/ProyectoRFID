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
        self.window.setWindowIcon(QIcon("./view/resources/cep-logo.png"))
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()
        self.view.app.exec_()

    def createGridLayout(self):
        self.layout = QGridLayout()

        btnSocio = QPushButton('Socios')
        btnSocio.setObjectName('botonHome')
        btnSocio.setIcon(QIcon("./view/resources/socio.png"))
        btnSocio.setIconSize(QSize(40,40))
        btnSocio.clicked.connect(self.view.mostrarModuloSocio)
        btnSocio.setMinimumWidth(200)

        btnAlumno = QPushButton('Alumnos')        
        btnAlumno.setObjectName('botonHome')
        btnAlumno.setIcon(QIcon("./view/resources/student.svg"))
        btnAlumno.setIconSize(QSize(40,40))        
        btnAlumno.clicked.connect(self.view.mostrarModuloAlumnos)
        btnAlumno.setMinimumWidth(200)        

        btnPrestamo = QPushButton('Prestamos')
        btnPrestamo.setObjectName('botonHome')
        btnPrestamo.setIcon(QIcon("./view/resources/loan.png"))
        btnPrestamo.setIconSize(QSize(40,40))
        btnPrestamo.setMinimumWidth(200)        

        btnVenta = QPushButton('Ventas')
        btnVenta.setObjectName('botonHome')
        btnVenta.setIcon(QIcon("./view/resources/sale.png"))
        btnVenta.setIconSize(QSize(40,40))        
        btnVenta.setMinimumWidth(200)        

        btnPromocion = QPushButton('Promociones')
        btnPromocion.setObjectName('botonHome')
        btnPromocion.setIcon(QIcon("./view/resources/promotions.png"))
        btnPromocion.setIconSize(QSize(40,40))                
        btnPromocion.setMinimumWidth(200)        

        btnCaja = QPushButton('Caja')
        btnCaja.setObjectName('botonHome')
        btnCaja.setIcon(QIcon("./view/resources/caja.jpg"))
        btnCaja.setIconSize(QSize(40,40))        
        btnCaja.setMinimumWidth(200)        

        btnEquipo = QPushButton('Equipos')
        btnEquipo.setObjectName('botonHome')
        btnEquipo.setIcon(QIcon("./view/resources/equipo.jpg"))
        btnEquipo.setIconSize(QSize(40,40))        
        btnEquipo.setMinimumWidth(200)        

        btnSalir = QPushButton('Salir')
        btnSalir.setObjectName('botonHome')
        btnSalir.setIcon(QIcon("./view/resources/exit.svg"))
        btnSalir.setIconSize(QSize(40,40))        
        btnSalir.setMinimumWidth(200)                
        btnSalir.clicked.connect(self.view.salir)

        labelTitle = QLabel('Sistema de Control del CEP')
        labelTitle.setObjectName('tituloHome')
        labelTitle.setAlignment(Qt.AlignCenter)

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
        #self.window.setFixedSize(self.window.size())
