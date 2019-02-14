from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os, math

class Alumnos:

    def __init__(self, view, paginaActual=1, cantidadElementos=10):
        self.view = view
        self.title = 'Alumnos | CEP'
        self.paginaActual = paginaActual
        self.cantidadElementos = cantidadElementos
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon('./view/resources/student.svg'))
        self.alumnos = self.view.generalController.alumnoController.listarAlumnoPaginado(self.paginaActual, self.cantidadElementos) 
        self.cantidadAlumnos = self.view.generalController.alumnoController.getCantidadAlumnos()
        self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)

        horizontalLayout = QHBoxLayout()

        btnPrimeraPagina = QPushButton("<<")
        btnPrimeraPagina.setObjectName("botonPrimario")
        btnPrimeraPagina.clicked.connect(self.firstPage)

        btnAnteriorPagina = QPushButton(" < ")
        btnAnteriorPagina.setObjectName("botonPrimario")
        btnAnteriorPagina.clicked.connect(self.previousPage)

        btnPaginaActual = QPushButton(" " + str(self.paginaActual) + " ")
        btnPaginaActual.setObjectName("botonPrimario")        

        btnSiguientePagina = QPushButton(" > ")
        btnSiguientePagina.setObjectName("botonPrimario")
        btnSiguientePagina.clicked.connect(self.nextPage)

        btnUltimaPagina = QPushButton(">>")
        btnUltimaPagina.setObjectName("botonPrimario")
        btnUltimaPagina.clicked.connect(self.lastPage)        

        horizontalLayout.addWidget(btnPrimeraPagina)
        horizontalLayout.addWidget(btnAnteriorPagina)
        horizontalLayout.addWidget(btnPaginaActual)        
        horizontalLayout.addWidget(btnSiguientePagina)           
        horizontalLayout.addWidget(btnUltimaPagina)

        labelTitle = QLabel("Alumnos")
        labelTitle.setObjectName("tituloModulo")

        btnNuevo = QPushButton("Nuevo")
        btnNuevo.setObjectName("botonPrimario")
        btnNuevo.setIcon(QIcon("./view/resources/add.svg"))
        btnNuevo.clicked.connect(self.view.mostrarFormAlumno)

        btnEliminar = QPushButton("Eliminar")
        btnEliminar.setObjectName("botonPrimario")
        btnEliminar.setIcon(QIcon("./view/resources/add.svg"))
        btnEliminar.clicked.connect(self.deleteStudents) 

        self.inputSearch = QLineEdit()
        self.inputSearch.setObjectName("inputSearch")
        self.inputSearch.setMaximumWidth(200)

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("botonPrimario")
        btnSearch.setIcon(QIcon("./view/resources/search.svg"))

        with open('./view/resources/styles.css') as f:
            labelTitle.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnSearch.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnPrimeraPagina.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnAnteriorPagina.setStyleSheet(f.read())                        
        with open('./view/resources/styles.css') as f:
            btnSiguientePagina.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnUltimaPagina.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnPaginaActual.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            self.inputSearch.setStyleSheet(f.read())                                    

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
        self.layout.addWidget(btnEliminar,1,1)        
        self.layout.addWidget(self.inputSearch,1,9)
        self.layout.addWidget(btnSearch,1,10)
        self.layout.addWidget(self.tablaAlumnos,2,0,1,11)
        self.layout.addLayout(horizontalLayout,3,9,1,2)
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

    def nextPage(self):
        if self.cantidadAlumnos is None or self.cantidadAlumnos <= 0:
            return
        cantPaginas = math.ceil(self.cantidadAlumnos/self.cantidadElementos)
        if self.paginaActual < cantPaginas:
            self.view.alumnosView = Alumnos(self.view, self.paginaActual+1)
            self.view.alumnosView.start()

    def previousPage(self):
        if self.paginaActual > 1:
            self.view.alumnosView = Alumnos(self.view, self.paginaActual-1)
            self.view.alumnosView.start()
        
    def firstPage(self):
        self.view.alumnosView = Alumnos(self.view, 1)
        self.view.alumnosView.start()
    
    def lastPage(self):
        if self.cantidadAlumnos is None or self.cantidadAlumnos <= 0:
            return
        cantPaginas = math.ceil(self.cantidadAlumnos/self.cantidadElementos)
        self.view.alumnosView = Alumnos(self.view,cantPaginas)
        self.view.alumnosView.start()
    
    def deleteStudents(self):
        select = self.tablaAlumnos.selectionModel()
        selectedRows = select.selectedRows()
        data = []
        for i in selectedRows:
            data.append(str(i.data()))
        res = self.view.generalController.alumnoController.eliminarAlumno(data)
        if res:
            self.view.mostrarModuloAlumnos()
