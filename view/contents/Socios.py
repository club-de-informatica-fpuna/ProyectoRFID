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
        self.socios = self.setState(self.view.generalController.socioController.listarSocios())
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)
        
        labelTitle = QLabel("Socios")

        btnNew = QPushButton("Nuevo")
        btnNew.setObjectName("botonPrimario")

        self.inputSearch = QLineEdit()
        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("botonPrimario")

        with open('./view/resources/styles.css') as f:
            btnSearch.setStyleSheet(f.read())

        self.partnerTable = QTableWidget()
        self.partnerTable.setRowCount(len(self.socios))
        self.partnerTable.setColumnCount(6)

        header = self.partnerTable.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.partnerTable.setHorizontalHeaderItem(0, QTableWidgetItem("UID"))
        self.partnerTable.setHorizontalHeaderItem(1, QTableWidgetItem("C.I."))
        self.partnerTable.setHorizontalHeaderItem(2, QTableWidgetItem("FECHA INGRESO"))
        self.partnerTable.setHorizontalHeaderItem(3, QTableWidgetItem("CARRERA"))
        self.partnerTable.setHorizontalHeaderItem(4, QTableWidgetItem("ESTADO"))
        self.partnerTable.setHorizontalHeaderItem(5, QTableWidgetItem("ACCIONES"))

        self.partnerTable.horizontalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")
        self.partnerTable.verticalHeader().setStyleSheet("QHeaderView::section {background: #002156; color: white; font-weight: bold; border: 1px solid silver; padding: 5px}")        
        self.partnerTable.setStyleSheet("border-top: 0px solid transparent; border-left: 0px solid transparent")

        for partner in self.socios:
            carrer = self.view.generalController.socioController.obtenerCarrera(partner.ci)
            self.partnerTable.setItem(self.socios.index(partner), 0, QTableWidgetItem(partner.uid))
            self.partnerTable.setItem(self.socios.index(partner), 1, QTableWidgetItem(partner.ci))
            self.partnerTable.setItem(self.socios.index(partner), 2, QTableWidgetItem(str(partner.fechaIngreso)))
            self.partnerTable.setItem(self.socios.index(partner), 3, QTableWidgetItem(carrer.denominacion))
            self.partnerTable.setItem(self.socios.index(partner), 4, QTableWidgetItem(partner.estado))
            self.partnerTable.setItem(self.socios.index(partner), 5, QTableWidgetItem(""))
        
        self.partnerTable.move(0, 0)

        self.layout.addWidget(labelTitle)
        self.layout.addWidget(btnNew)
        self.layout.addWidget(self.inputSearch)
        self.layout.addWidget(btnSearch)
        self.layout.addWidget(self.partnerTable)
        self.layout.setAlignment(Qt.AlignTop)



    def center(self):
        screen = QDesktopWidget().screenGeometry()
        width = (screen.width()-screen.width()/8)
        height = (screen.height()-screen.height()/8)
        self.window.setGeometry( (screen.width()-width) /2, (screen.height()-height)/2, width, height)

    def setState(self, socio):
        for s in socio:
            s.estado = "A" if s.estado else "I"
        return socio