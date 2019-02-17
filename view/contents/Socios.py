from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os

class Socio:

    def __init__(self, view):
        self.view = view
        self.title = 'Socios | CEP'

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon('./view/resources/socio.png'))
        self.socios = self.setState(self.view.generalController.socioController.listarSocios())
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)
        
        labelTitle = QLabel("Socios")
        labelTitle.setObjectName("tituloModulo")

        with open('./view/resources/styles.css') as f:
            labelTitle.setStyleSheet(f.read())        

        btnNew = QPushButton("Nuevo")
        btnNew.setObjectName("botonPrimario")
        btnNew.clicked.connect(self.view.mostrarFormSocio)

        btnRemove = QPushButton("Eliminar")
        btnRemove.setObjectName("cancel")
        btnRemove.clicked.connect(self.removePartner)

        with open('./view/resources/styles.css') as f:
            btnNew.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnRemove.setStyleSheet(f.read())

        self.inputSearch = QLineEdit()
        self.inputSearch.setObjectName("inputSearch")
        self.inputSearch.setMaximumWidth(200)

        btnSearch = QPushButton("Buscar")
        btnSearch.clicked.connect(self.buscarSocio)
        btnSearch.setObjectName("botonPrimario")

        with open('./view/resources/styles.css') as f:
            self.inputSearch.setStyleSheet(f.read())

        with open('./view/resources/styles.css') as f:
            btnSearch.setStyleSheet(f.read())

        self.partnerTable = QTableWidget()
        self.partnerTable.setRowCount(len(self.socios))
        self.partnerTable.setColumnCount(6)

        header = self.partnerTable.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.partnerTable.setHorizontalHeaderItem(0, QTableWidgetItem("C.I."))
        self.partnerTable.setHorizontalHeaderItem(1, QTableWidgetItem("UID"))
        self.partnerTable.setHorizontalHeaderItem(2, QTableWidgetItem("FECHA INGRESO"))
        self.partnerTable.setHorizontalHeaderItem(3, QTableWidgetItem("CARRERA"))
        self.partnerTable.setHorizontalHeaderItem(4, QTableWidgetItem("ESTADO"))
        self.partnerTable.setHorizontalHeaderItem(5, QTableWidgetItem("ACCIONES"))

        self.partnerTable.horizontalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")
        self.partnerTable.verticalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")        
        self.partnerTable.setStyleSheet("border-top: 0px solid transparent; border-left: 0px solid transparent")

        for partner in self.socios:
            carrer = self.view.generalController.socioController.obtenerCarrera(partner.ci)
            self.partnerTable.setItem(self.socios.index(partner), 0, QTableWidgetItem(partner.ci))
            self.partnerTable.setItem(self.socios.index(partner), 1, QTableWidgetItem(partner.uid))
            self.partnerTable.setItem(self.socios.index(partner), 2, QTableWidgetItem(str(partner.fechaIngreso)))
            self.partnerTable.setItem(self.socios.index(partner), 3, QTableWidgetItem(carrer.denominacion))
            self.partnerTable.setItem(self.socios.index(partner), 4, QTableWidgetItem(partner.estado))
            self.partnerTable.setItem(self.socios.index(partner), 5, QTableWidgetItem(""))
        
        self.partnerTable.move(0, 0)

        self.layout.addWidget(labelTitle, 0, 0, 1, 10)
        self.layout.addWidget(btnNew, 1, 0)
        self.layout.addWidget(btnRemove, 1, 1)
        self.layout.addWidget(self.inputSearch, 1, 8)
        self.layout.addWidget(btnSearch, 1, 9)
        self.layout.addWidget(self.partnerTable, 2, 0, 1, 10)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaGeneral")
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())

    def removePartner(self):
        choices    = self.partnerTable.selectionModel()
        selections = choices.selectedRows()

        data = []
        for i in selections:
            data.append(str(i.data()))

        response = self.view.generalController.socioController.eliminarSocioCi(data)
        if response:
            self.view.mostrarModuloSocio()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        width = (screen.width()-screen.width()/8)
        height = (screen.height()-screen.height()/8)
        self.window.setGeometry( (screen.width()-width) /2, (screen.height()-height)/2, width, height)

    def setState(self, socio):
        for s in socio:
            s.estado = "A" if s.estado else "I"
        return socio
    
    def buscarSocio(self):
        ciSocio = self.inputSearch.text()
        socio = self.view.generalController.socioController.obtenerSocioCi(ciSocio)
        if socio is not None:
            alumno = self.view.generalController.alumnoController.buscarAlumno(ciSocio)
            carrera = self.view.generalController.socioController.obtenerCarrera(ciSocio)
            if alumno is not None and carrera is not None:
                self.view.mostrarConsultaSocio(socio, alumno, carrera)