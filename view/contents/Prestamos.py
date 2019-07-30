from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os, math

class Prestamos:

    def __init__(self, view, paginaActual=1, cantidadElementos=15):
        self.view = view
        self.title = 'Préstamos | CEP'
        self.paginaActual = paginaActual
        self.cantidadElementos = cantidadElementos
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon('./view/resources/student.svg'))
        self.prestamos = self.view.generalController.prestamoController.listarPrestamoPaginado(self.paginaActual, self.cantidadElementos) 
        self.cantidadPrestamos = self.view.generalController.prestamoController.getCantidadPrestamo()
        self.createGridLayout()
        self.center()


    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):
        self.layout = QGridLayout(self.window)
        pathIcons    = "./view/resources/icons/"
        pathResource = "./view/resources/"

        horizontalLayout = QHBoxLayout()

        btnPrimeraPagina = QPushButton("«")
        btnPrimeraPagina.setObjectName("page")
        btnPrimeraPagina.clicked.connect(self.firstPage)

        btnAnteriorPagina = QPushButton(" ‹ ")
        btnAnteriorPagina.setObjectName("page")
        btnAnteriorPagina.clicked.connect(self.previousPage)

        btnPaginaActual = QPushButton(" " + str(self.paginaActual) + " ")
        btnPaginaActual.setObjectName("page")        

        btnSiguientePagina = QPushButton(" › ")
        btnSiguientePagina.setObjectName("page")
        btnSiguientePagina.clicked.connect(self.nextPage)

        btnUltimaPagina = QPushButton("»")
        btnUltimaPagina.setObjectName("page")
        btnUltimaPagina.clicked.connect(self.lastPage)        

        horizontalLayout.addWidget(btnPrimeraPagina)
        horizontalLayout.addWidget(btnAnteriorPagina)
        horizontalLayout.addWidget(btnPaginaActual)        
        horizontalLayout.addWidget(btnSiguientePagina)           
        horizontalLayout.addWidget(btnUltimaPagina)

        labelTitle = QLabel("Préstamos")
        labelTitle.setObjectName("tituloModulo")

        labelFooter = QLabel("Total de prestamos: " + str(self.cantidadPrestamos))
        labelFooter.setObjectName("tituloPopup")

        btnNuevo = QPushButton("Registrar")
        btnNuevo.setObjectName("botonPrimario")
        btnNuevo.setIcon(QIcon(pathIcons + "add-student.png"))
        btnNuevo.clicked.connect(self.view.mostrarFormPrestamo)

        shortcutNuevo = QShortcut(QKeySequence(Qt.Key_Return), btnNuevo)
        shortcutNuevo.setContext(Qt.WidgetShortcut)
        shortcutNuevo.activated.connect(self.view.mostrarFormPrestamo)

        btnEliminar = QPushButton("Eliminar")
        btnEliminar.setObjectName("cancel")
        btnEliminar.setIcon(QIcon(pathIcons + "remove.png"))
        btnEliminar.clicked.connect(self.deleteStudents) 

        shortcutEliminar = QShortcut(QKeySequence(Qt.Key_Return), btnEliminar)
        shortcutEliminar.setContext(Qt.WidgetShortcut)
        shortcutEliminar.activated.connect(self.deleteStudents)      

        btnBuscar = QPushButton("Buscar")
        btnBuscar.setObjectName("search")
        btnBuscar.setIcon(QIcon(pathIcons + "search.png"))
        btnBuscar.clicked.connect(self.deleteStudents) 

        shortcutBuscar = QShortcut(QKeySequence(Qt.Key_Return), btnBuscar)
        shortcutBuscar.setContext(Qt.WidgetShortcut)
        ##shortcutBuscar.activated.connect(self.deleteStudents)            

        btnEditar = QPushButton("Editar")
        btnEditar.setObjectName("botonSecundario")
        btnEditar.setIcon(QIcon(pathIcons + "edit.png"))
        btnEditar.clicked.connect(self.manejarEditar)

        shortcutEditar = QShortcut(QKeySequence(Qt.Key_Return), btnEditar)
        shortcutEditar.setContext(Qt.WidgetShortcut)
        shortcutEditar.activated.connect(self.manejarEditar)               

        self.inputSearch = QLineEdit(self.window)
        self.inputSearch.setObjectName("inputSearch")
        self.inputSearch.setPlaceholderText("Ingrese su CI")
        self.inputSearch.setMaximumWidth(300)
        
        shortcutSearch = QShortcut(QKeySequence(Qt.Key_Return), self.inputSearch)
        shortcutSearch.setContext(Qt.WidgetShortcut)
        shortcutSearch.activated.connect(self.manejarBuscar)

        shortcutSearchIntro = QShortcut(QKeySequence(Qt.Key_Enter), self.inputSearch)
        shortcutSearchIntro.setContext(Qt.WidgetShortcut)
        shortcutSearchIntro.activated.connect(self.manejarBuscar)        

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("searchModuleButton")
        btnSearch.setIcon(QIcon(pathIcons + "search.png"))
        btnSearch.setFixedSize(80, 32)
        btnSearch.clicked.connect(self.manejarBuscar)

        shortcutBuscar = QShortcut(QKeySequence(Qt.Key_Return), btnSearch)
        shortcutBuscar.setContext(Qt.WidgetShortcut)
        shortcutBuscar.activated.connect(self.manejarEditar)          

        with open(pathResource +"styles.css") as f:
            labelTitle.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnSearch.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnPrimeraPagina.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnAnteriorPagina.setStyleSheet(f.read())                        
        with open(pathResource +"styles.css") as f:
            btnSiguientePagina.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnUltimaPagina.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnPaginaActual.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            self.inputSearch.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            btnEditar.setStyleSheet(f.read())
        with open(pathResource +"styles.css") as f:
            labelFooter.setStyleSheet(f.read())

        self.tablaPrestamos = QTableWidget(self.window)
        self.tablaPrestamos.setRowCount(len(self.prestamos))
        self.tablaPrestamos.setColumnCount(8)

        header = self.tablaPrestamos.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.tablaPrestamos.setHorizontalHeaderItem(0, QTableWidgetItem("EQUIPO"))
        self.tablaPrestamos.setHorizontalHeaderItem(1, QTableWidgetItem("RESPONSABLE"))
        self.tablaPrestamos.setHorizontalHeaderItem(2, QTableWidgetItem("C.I."))
        self.tablaPrestamos.setHorizontalHeaderItem(3, QTableWidgetItem("TELÉFONO"))
        self.tablaPrestamos.setHorizontalHeaderItem(4, QTableWidgetItem("CARRERA"))
        self.tablaPrestamos.setHorizontalHeaderItem(5, QTableWidgetItem("F. PRÉSTAMO"))
        self.tablaPrestamos.setHorizontalHeaderItem(6, QTableWidgetItem("F. DEVOLUCIÓN"))
        self.tablaPrestamos.setHorizontalHeaderItem(7, QTableWidgetItem("ESTADO"))



        self.tablaPrestamos.horizontalHeader().setStyleSheet("QHeaderView::section {background: #0e52c0; color: #fff; font-weight: bold; border: 1px solid #f7f7f7; padding: 5px}")
        self.tablaPrestamos.verticalHeader().setStyleSheet("QHeaderView::section {background: #0e52c0; color: #fff; font-weight: bold; border: 1px solid #f7f7f7; padding: 5px}")
        self.tablaPrestamos.setStyleSheet("border-top: 0px transparent; border-left: 0px transparent")

        self.tablaPrestamos.setFocus()
        self.tablaPrestamos.selectRow(0)

        count = 0
        for i in self.prestamos:
##            carrera = self.view.generalController.carreraController.listarCarreraPorId(i.idCarrera)
            self.tablaPrestamos.setItem(count,0,QTableWidgetItem(i.descripcion))
            self.tablaPrestamos.setItem(count,1,QTableWidgetItem(i.nombre + " " + i.apellido))
            self.tablaPrestamos.setItem(count,2,QTableWidgetItem(str(i.ci)))
            self.tablaPrestamos.setItem(count,3,QTableWidgetItem(i.telefono))
            self.tablaPrestamos.setItem(count,4,QTableWidgetItem(i.denominacion))
            self.tablaPrestamos.setItem(count,5,QTableWidgetItem(i.fecha_prestamo))
            self.tablaPrestamos.setItem(count,6,QTableWidgetItem(i.fecha_devolucion))
            self.tablaPrestamos.setItem(count,7,QTableWidgetItem(str(i.estado)))
            count = count + 1
        self.tablaPrestamos.move(0,0)

        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.inputSearch)
        searchLayout.addWidget(btnSearch)
        
        self.layout.addWidget(labelTitle, 0, 0, 1, 10)
        self.layout.addWidget(btnNuevo, 1, 0)
        self.layout.addWidget(btnBuscar, 1, 1) 
        self.layout.addWidget(btnEditar, 1, 3) 
        self.layout.addWidget(btnEliminar, 1, 2)
        self.layout.addLayout(searchLayout, 1, 9, 1, 2)
        self.layout.addWidget(self.tablaPrestamos, 2, 0, 1, 11)
        self.layout.addWidget(labelFooter, 3, 0, 1, 2)
        self.layout.addLayout(horizontalLayout, 3, 10, 1, 1)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaGeneral")
        with open(pathResource +"styles.css") as f:
            self.window.setStyleSheet(f.read())

        shortcutKSearch = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), self.window)
        shortcutKSearch.setContext(Qt.WindowShortcut)
        shortcutKSearch.activated.connect(self.inputSearch.setFocus) 

        shortcutNextPage = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Right), self.window)
        shortcutNextPage.setContext(Qt.WindowShortcut)
        shortcutNextPage.activated.connect(self.nextPage)

        shortcutPrevPage = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Left), self.window)
        shortcutPrevPage.setContext(Qt.WindowShortcut)
        shortcutPrevPage.activated.connect(self.previousPage)                    

        shortcutKNuevo = QShortcut(QKeySequence(Qt.Key_F1), self.window)
        shortcutKNuevo.setContext(Qt.WindowShortcut)
        shortcutKNuevo.activated.connect(self.view.mostrarFormPrestamo)

        shortcutKEliminar = QShortcut(QKeySequence(Qt.Key_F2), self.window)
        shortcutKEliminar.setContext(Qt.WindowShortcut)
        shortcutKEliminar.activated.connect(self.deleteStudents)

        shortcutKEditar = QShortcut(QKeySequence(Qt.Key_F3), self.window)
        shortcutKEditar.setContext(Qt.WindowShortcut)
        shortcutKEditar.activated.connect(self.manejarEditar)

        shortcutSalir = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcutSalir.setContext(Qt.WindowShortcut)
        shortcutSalir.activated.connect(self.window.hide)
        
    def center(self):
        self.window.showMaximized()

    def nextPage(self):
        if self.cantidadPrestamos is None or self.cantidadPrestamos <= 0:
            return
        cantPaginas = math.ceil(self.cantidadPrestamos/self.cantidadElementos)
        if self.paginaActual < cantPaginas:
            self.view.prestamosView = Prestamos(self.view, self.paginaActual+1)
            self.view.prestamosView.start()

    def previousPage(self):
        if self.paginaActual > 1:
            self.view.prestamosView = Prestamos(self.view, self.paginaActual-1)
            self.view.prestamosView.start()
        
    def firstPage(self):
        self.view.prestamosView = Prestamos(self.view, 1)
        self.view.prestamosView.start()
    
    def lastPage(self):
        if self.cantidadprestamos is None or self.cantidadprestamos <= 0:
            return
        cantPaginas = math.ceil(self.cantidadprestamos/self.cantidadElementos)
        self.view.prestamosView = Prestamos(self.view,cantPaginas)
        self.view.prestamosView.start()
    
    def deleteStudents(self):
        select = self.tablaPrestamos.selectionModel()
        selectedRows = select.selectedRows()
        data = []
        for i in selectedRows:
            data.append(str(i.data()))
        if len(data) == 0:
            self.view.mostrarPopup("Atención", "Atención", "Debes seleccionar el conjunto de prestamos a eliminar")
            return
        else:
            qm = QMessageBox
            ret = qm.question(self.window,"Confirmación", "¿Desea eliminar los registros seleccionados?", qm.Yes | qm.No)
            if ret == qm.Yes:
                res = self.view.generalController.prestamoController.eliminarprestamo(data)
                if res is True:
                    self.view.mostrarModuloPrestamo()
                else:
                    self.view.mostrarPopup("Atención", "No se puede eliminar", "El prestamo es socio, primero debes desasociar al prestamo")

    def manejarEditar(self):
        select = self.tablaPrestamos.selectionModel()
        selectedRows = select.selectedRows()
        data = []
        for i in selectedRows:
            data.append(str(i.data()))
        if len(data) == 0:
            self.view.mostrarPopup("Atención", "Atención", "Debes seleccionar el préstamo a editar")
            return    
        prestamo = self.view.generalController.prestamoController.buscarprestamo(data[0])        
        if prestamo is not None:
            carrera = self.view.generalController.prestamoController.obtenerCarrera(prestamo.ci)
            self.view.mostrarFormprestamo(title="Actualizar préstamo | CEP", update=True, prestamoUpdate=prestamo, raceById=carrera)


    def manejarBuscar(self):
        inputCi = self.inputSearch.text()
        prestamo = self.view.generalController.prestamoController.buscarprestamo(inputCi)
        if prestamo is not None:
            carrera = self.view.generalController.prestamoController.obtenerCarrera(prestamo.ci)
            self.view.mostrarFormprestamo(title="Ver prestamo | CEP", update=True, prestamoUpdate=prestamo, editable=False, raceById=carrera)
        else:
            messageNotFount = "El prestamo con cedula [{}] no existe o aún no ha sido registrado".format(inputCi)
            messageStrEmpty = "Debe ingersar un número de cedula para iniciar con la busqueda"
            self.view.mostrarPopup("Datos no encontrados", "Detalle",messageNotFount if inputCi is not '' else messageStrEmpty)