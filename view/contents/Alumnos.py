from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os

class Alumnos:

    def __init__(self, view):
        self.view = view
        self.title = 'Alumnos | CEP'
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.alumnos = self.view.generalController.alumnoController.listarAlumno()        
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)

        labelTitle = QLabel("Alumnos")
        labelTitle.setObjectName("tituloModulo")

        btnNuevo = QPushButton("Nuevo")
        btnNuevo.setObjectName("botonPrimario")
        btnNuevo.clicked.connect(self.view.mostrarFormAlumno)

        inputSearch = QLineEdit()

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("botonPrimario")        

        with open('./view/resources/styles.css') as f:
            labelTitle.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnSearch.setStyleSheet(f.read())

        self.tablaAlumnos = QTableWidget()
        self.tablaAlumnos.setRowCount(len(self.alumnos))

        self.tablaAlumnos.setColumnCount(6)

        header = self.tablaAlumnos.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.tablaAlumnos.setHorizontalHeaderItem(0, QTableWidgetItem("CI"))
        self.tablaAlumnos.setHorizontalHeaderItem(1, QTableWidgetItem("NOMBRE Y APELLIDO"))
        self.tablaAlumnos.setHorizontalHeaderItem(2, QTableWidgetItem("EMAIL"))
        self.tablaAlumnos.setHorizontalHeaderItem(3, QTableWidgetItem("TELÉFONO"))
        self.tablaAlumnos.setHorizontalHeaderItem(4, QTableWidgetItem("CARRERA"))
        self.tablaAlumnos.setHorizontalHeaderItem(5, QTableWidgetItem("ACCIONES"))

        self.tablaAlumnos.horizontalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")
        self.tablaAlumnos.verticalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")        
        self.tablaAlumnos.setStyleSheet("border-top: 0px solid transparent; border-left: 0px solid transparent")

        count = 0
        for i in self.alumnos:
            carrera = self.view.generalController.carreraController.listarCarreraPorId(i.idCarrera)
            self.tablaAlumnos.setItem(count,0,QTableWidgetItem(str(i.ci)))
            self.tablaAlumnos.setItem(count,1,QTableWidgetItem(i.nombre + " " + i.apellido))
            self.tablaAlumnos.setItem(count,2,QTableWidgetItem(i.email))
            self.tablaAlumnos.setItem(count,3,QTableWidgetItem(i.telefono))
            self.tablaAlumnos.setItem(count,4,QTableWidgetItem(carrera.denominacion))
            self.tablaAlumnos.setItem(count,5,QTableWidgetItem(""))            
            count = count + 1
        self.tablaAlumnos.move(0,0)
        
        self.layout.addWidget(labelTitle,0,0,1,10)
        self.layout.addWidget(btnNuevo,1,0)
        self.layout.addWidget(inputSearch,1,8)
        self.layout.addWidget(btnSearch,1,9)
        self.layout.addWidget(self.tablaAlumnos,2,0,1,10)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaGeneral")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        width = (screen.width()-screen.width()/8)
        height = (screen.height()-screen.height()/8)
        self.window.setGeometry( (screen.width()-width) /2, (screen.height()-height)/2, width, height)       