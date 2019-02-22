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
        iconSocio = QIcon("./view/resources/partner.svg")
        btnSocio.setIcon(iconSocio)
        btnSocio.setIconSize(QSize(40,40))
        btnSocio.clicked.connect(self.view.mostrarModuloSocio)
        btnSocio.setMinimumWidth(200)
        btnSocio.setMaximumWidth(300)

        btnAlumno = QPushButton('Alumnos')        
        btnAlumno.setObjectName('botonHome')
        btnAlumno.setIcon(QIcon("./view/resources/student.svg"))
        btnAlumno.setIconSize(QSize(40,40))        
        btnAlumno.clicked.connect(self.view.mostrarModuloAlumnos)
        btnAlumno.setMinimumWidth(200)
        btnAlumno.setMaximumWidth(300)

        btnPrestamo = QPushButton('Prestamos')
        btnPrestamo.setObjectName('botonHome')
        btnPrestamo.setIcon(QIcon("./view/resources/loan.svg"))
        btnPrestamo.setIconSize(QSize(40,40))
        btnPrestamo.setMinimumWidth(200)
        btnPrestamo.setMaximumWidth(300)

        btnVenta = QPushButton('Ventas')
        btnVenta.setObjectName('botonHome')
        btnVenta.setIcon(QIcon("./view/resources/sale.svg"))
        btnVenta.setIconSize(QSize(40,40))        
        btnVenta.setMinimumWidth(200)
        btnVenta.setMaximumWidth(300)                

        btnPromocion = QPushButton('Promociones')
        btnPromocion.setObjectName('botonHome')
        btnPromocion.setIcon(QIcon("./view/resources/promotions-alter.svg"))
        btnPromocion.setIconSize(QSize(40,40))                
        btnPromocion.setMinimumWidth(200)
        btnPromocion.setMaximumWidth(300)                

        btnCaja = QPushButton('Caja')
        btnCaja.setObjectName('botonHome')
        btnCaja.setIcon(QIcon("./view/resources/box.svg"))
        btnCaja.setIconSize(QSize(40,40))        
        btnCaja.setMinimumWidth(200)
        btnCaja.setMaximumWidth(300)

        btnEquipo = QPushButton('Equipos')
        btnEquipo.setObjectName('botonHome')
        btnEquipo.setIcon(QIcon("./view/resources/elements.svg"))
        btnEquipo.setIconSize(QSize(40,40))        
        btnEquipo.setMinimumWidth(200) 
        btnEquipo.setMaximumWidth(300)               

        btnConfiguracion = QPushButton('Configuración')
        btnConfiguracion.setObjectName('botonHome')
        btnConfiguracion.setIcon(QIcon("./view/resources/config.svg"))
        btnConfiguracion.setIconSize(QSize(40,40))        
        btnConfiguracion.setMinimumWidth(200)
        btnConfiguracion.setMaximumWidth(300)                   
        btnConfiguracion.clicked.connect(self.view.mostrarConfiguracion)

        btnAcercaDe = QPushButton('Acerca de')
        btnAcercaDe.setObjectName('botonHome')
        btnAcercaDe.setIcon(QIcon("./view/resources/about-other.svg"))
        btnAcercaDe.setIconSize(QSize(40,40))
        btnAcercaDe.setMinimumWidth(200)
        btnAcercaDe.setMaximumWidth(300)                   

        btnSalir = QPushButton('Salir')
        btnSalir.setObjectName('botonHome')
        btnSalir.setIcon(QIcon("./view/resources/exit-alter.svg"))
        btnSalir.setIconSize(QSize(40,40))        
        btnSalir.setMinimumWidth(200)
        btnSalir.setMaximumWidth(300)                   
        btnSalir.clicked.connect(self.view.salir)

        labelTitle = QLabel('SISTEMA DE CONTROL DEL CEP')
        labelTitle.setWordWrap(True)
        labelTitle.setObjectName('tituloHome')
        labelTitle.setAlignment(Qt.AlignCenter)

        labelFooter = QLabel('Centro de Estudiantes de la Facultad Politécnica de la Universidad Nacional de Asunción')
        labelFooter.setObjectName('footerHome')
        labelFooter.setWordWrap(True)
        labelFooter.setAlignment(Qt.AlignCenter)

        with open('./view/resources/styles.css') as f:
            labelFooter.setStyleSheet(f.read())
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
        pixmap_resized = pixMap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        labelImg.setPixmap(pixmap_resized)
        labelImg.setStyleSheet('margin:auto')

        labelLogoClub = QLabel()
        pixmap = QPixmap("./view/resources/logo-club-circulo.png")
        pixmap = pixmap.scaled(120,120, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        labelLogoClub.setPixmap(pixmap)

        labelLogoFPUNA = QLabel()
        pixmap = QPixmap("./view/resources/logo-fpuna.png")
        pixmap = pixmap.scaled(90,120, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        labelLogoFPUNA.setPixmap(pixmap)        

        layoutFooter = QHBoxLayout()
        layoutFooter.addWidget(labelLogoClub)
        layoutFooter.addStretch()        
        layoutFooter.addWidget(labelFooter)
        layoutFooter.addStretch()        
        layoutFooter.addWidget(labelLogoFPUNA)      
        layoutFooter.setAlignment(labelFooter, Qt.AlignVCenter)
                
        layoutFooter.setContentsMargins(10,30,10,10)

        self.layout.addWidget(labelTitle, 0, 0, 1, 3)
        self.layout.addWidget(btnSocio, 1, 0, 1, 1, Qt.AlignRight)
        self.layout.addWidget(btnAlumno, 1, 2, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(btnPrestamo, 2, 0, 1, 1, Qt.AlignRight)
        self.layout.addWidget(btnVenta, 2, 2, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(btnPromocion, 3, 0, 1, 1, Qt.AlignRight)
        self.layout.addWidget(btnCaja, 3, 2, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(btnEquipo, 4, 0, 1, 1, Qt.AlignRight)
        self.layout.addWidget(btnConfiguracion, 4, 2, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(btnAcercaDe, 5, 0, 1, 1, Qt.AlignRight)        
        self.layout.addWidget(btnSalir, 5, 2, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(labelImg, 1, 1, 5, 1)
        self.layout.addLayout(layoutFooter,6,0,1,3, Qt.AlignLeft)

        self.layout.setContentsMargins(50, 20, 50, 20)
        self.layout.setAlignment(Qt.AlignCenter)

        labelImg.setAlignment(Qt.AlignCenter)
        labelImg.setMaximumWidth(200)

        labelTitle.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        labelFooter.setAlignment(Qt.AlignCenter | Qt.AlignBottom)

        self.window.setObjectName("ventanaHome")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())        
        self.window.setLayout(self.layout)

    def center(self):
        self.window.showFullScreen()