from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os, math

class Socio:

    def __init__(self, view, actualPage=1, quantityElements=15):
        self.view = view
        self.title = 'Socios | CEP'
        self.actualPage = actualPage
        self.quantityElements = quantityElements

    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.window.setWindowIcon(QIcon('./view/resources/partner.svg'))
        self.socios = self.setState(self.view.generalController.socioController.listarSocios(self.quantityElements, self.actualPage))
        self.totalPartner = self.view.generalController.socioController.numberOfPartners()
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

        labelTitle = QLabel("Socios")
        labelTitle.setObjectName("tituloModulo")

        total = QLabel("Total de Socios: "+str(self.totalPartner))
        total.setObjectName("tituloPopup")

        with open(pathResource + "styles.css") as f:
            labelTitle.setStyleSheet(f.read())

        with open(pathResource + "styles.css") as f:
            total.setStyleSheet(f.read())       

        btnNew = QPushButton("Nuevo")
        btnNew.setObjectName("botonPrimario")
        btnNew.setIcon(QIcon(pathIcons + "add-partner.png"))
        btnNew.clicked.connect(self.view.mostrarFormSocio)

        btnRemove = QPushButton("Eliminar")
        btnRemove.setObjectName("cancel")
        btnRemove.setIcon(QIcon(pathIcons + "remove.png"))
        btnRemove.clicked.connect(self.removePartner)

        btnEdit = QPushButton("Modificar")
        btnEdit.setObjectName("botonSecundario")
        btnEdit.setIcon(QIcon(pathIcons + "edit.png"))
        btnEdit.clicked.connect(self.editPartner)

        with open(pathResource + "styles.css") as f:
            btnNew.setStyleSheet(f.read())
        with open(pathResource + "styles.css") as f:
            btnRemove.setStyleSheet(f.read())
        with open(pathResource + "styles.css") as f:
            btnEdit.setStyleSheet(f.read())

        self.inputSearch = QLineEdit()
        self.inputSearch.setObjectName("inputSearch")
        self.inputSearch.setPlaceholderText("Ingrese su CI")
        self.inputSearch.setFocus(True)
        self.inputSearch.setToolTip("Ingrese número de sedula para buscar")
        
        self.inputSearch.setMaximumWidth(300)

        btnSearch = QPushButton("Buscar")
        btnSearch.setObjectName("searchModuleButton")
        btnSearch.setIcon(QIcon(pathIcons + "search.png"))
        btnSearch.setFixedSize(80, 32)
        btnSearch.clicked.connect(self.buscarSocio)

        with open(pathResource + "styles.css") as f:
            self.inputSearch.setStyleSheet(f.read())

        with open(pathResource + "styles.css") as f:
            btnSearch.setStyleSheet(f.read())

        self.partnerTable = QTableWidget()
        self.partnerTable.setRowCount(len(self.socios))
        self.partnerTable.setColumnCount(6)

        header = self.partnerTable.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.partnerTable.setHorizontalHeaderItem(0, QTableWidgetItem("C.I."))
        self.partnerTable.setHorizontalHeaderItem(1, QTableWidgetItem("NOMBRE APELLIDO"))
        self.partnerTable.setHorizontalHeaderItem(2, QTableWidgetItem("UID"))
        self.partnerTable.setHorizontalHeaderItem(3, QTableWidgetItem("FECHA INGRESO"))
        self.partnerTable.setHorizontalHeaderItem(4, QTableWidgetItem("ESTADO"))
        self.partnerTable.setHorizontalHeaderItem(5, QTableWidgetItem("CARRERA"))
        

        self.partnerTable.horizontalHeader().setStyleSheet("QHeaderView::section {background: #0e52c0; color: #fff; font-weight: bold; border: 1px solid #f7f7f7; padding: 5px}")
        self.partnerTable.verticalHeader().setStyleSheet("QHeaderView::section {background: #0e52c0; color: #fff; font-weight: bold; border: 1px solid #f7f7f7; padding: 5px}")
        self.partnerTable.setStyleSheet("border-top: 0px solid transparent; border-left: 0px solid transparent")
        self.partnerTable.setFocus()
        self.partnerTable.selectRow(0)

        for partner in self.socios:
            alumno = self.view.generalController.socioController.obtenerAlumno(partner.ci)
            self.partnerTable.setItem(self.socios.index(partner), 0, QTableWidgetItem(partner.ci))
            self.partnerTable.setItem(self.socios.index(partner), 1, QTableWidgetItem(alumno.nombre +" "+ alumno.apellido))
            self.partnerTable.setItem(self.socios.index(partner), 2, QTableWidgetItem(partner.uid))
            self.partnerTable.setItem(self.socios.index(partner), 3, QTableWidgetItem(str(partner.fechaIngreso)))
            self.partnerTable.setItem(self.socios.index(partner), 4, QTableWidgetItem(partner.estado))
            self.partnerTable.setItem(self.socios.index(partner), 5, QTableWidgetItem(alumno.idCarrera.denominacion))

        self.partnerTable.move(0, 0)




        btnPrimeraPagina = QPushButton("«")
        btnPrimeraPagina.setObjectName("page")
        btnPrimeraPagina.clicked.connect(self.firstPage)

        btnAnteriorPagina = QPushButton(" ‹ ")
        btnAnteriorPagina.setObjectName("page")
        btnAnteriorPagina.clicked.connect(self.previousPage)

        btnPaginaActual = QPushButton(" " + str(self.actualPage) + " ")
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

        with open(pathResource + "styles.css") as f:
            btnPrimeraPagina.setStyleSheet(f.read())
        with open(pathResource + "styles.css") as f:
            btnAnteriorPagina.setStyleSheet(f.read())                        
        with open(pathResource + "styles.css") as f:
            btnSiguientePagina.setStyleSheet(f.read())
        with open(pathResource + "styles.css") as f:
            btnUltimaPagina.setStyleSheet(f.read())
        with open(pathResource + "styles.css") as f:
            btnPaginaActual.setStyleSheet(f.read())

        self.layout.addWidget(labelTitle, 0, 0, 1, 10)
        self.layout.addWidget(btnNew, 1, 0)
        self.layout.addWidget(btnEdit, 1, 1)
        self.layout.addWidget(btnRemove, 1, 2)
        self.layout.addWidget(self.inputSearch, 1, 9)
        self.layout.addWidget(btnSearch, 1, 10)
        self.layout.addWidget(self.partnerTable, 2, 0, 1, 11)
        self.layout.addWidget(total,3,0,1,2)
        self.layout.addLayout(horizontalLayout, 3, 10, 1, 1)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaGeneral")
        with open(pathResource + "styles.css") as f:
            self.window.setStyleSheet(f.read())

    def editPartner(self):
        select = self.partnerTable.selectionModel()
        selectedRows = select.selectedRows()
        if not selectedRows:
            self.view.mostrarPopup("Atención", "Atención", "Debes seleccionar al menos un registro para poder editar")
            return
        else:
            if len(selectedRows) > 1:
                self.view.mostrarPopup("Atención", "Atención", "Solo puedes seleccionar un registros para editar")
                return
            else:
                ciPartner = selectedRows[0].data()
                windowTitle = "Editar Socio | CEP"
                socio = self.view.generalController.socioController.obtenerSocioCi(ciPartner)
                alumno = self.view.generalController.alumnoController.buscarAlumno(ciPartner)
                carrera = self.view.generalController.socioController.obtenerCarrera(ciPartner)
                if socio is not None:
                    self.view.mostrarFormSocio(windowTitle, True, socio, alumno, carrera)
                else:
                    self.view.mostrarPopup("Error", "Ha ocurrido un error", "Ha ocurrido un error al obtener los datos solicitados")
                    return

    def removePartner(self):
        choices    = self.partnerTable.selectionModel()
        selections = choices.selectedRows()

        data = []
        for i in selections:
            data.append(str(i.data()))

        if len(data) == 0:
            self.view.mostrarPopup("Atención", "Atención", "Debes seleccionar al menos uno para poder eliminar")
            return
        else:
            qm = QMessageBox
            response = qm.question(self.window, "Confirmación", "¿Desea eliminar los registros?", qm.Yes | qm.No)
            if response == qm.Yes:
                res = self.view.generalController.socioController.eliminarSocioCi(data)
                if res :
                    self.view.mostrarModuloSocio()
                else:
                    self.view.mostrarPopup("Atención", "Error", "No se puede eliminar")

    def buscarSocio(self):
        ciSocio = self.inputSearch.text()
        socio = self.view.generalController.socioController.obtenerSocioCi(ciSocio)
        if socio is not None:
            alumno = self.view.generalController.alumnoController.buscarAlumno(ciSocio)
            carrera = self.view.generalController.socioController.obtenerCarrera(ciSocio)
            if alumno is not None and carrera is not None:
                self.view.mostrarConsultaSocio(socio, alumno, carrera)
        else:
            messageNotFount = "No se encuentra registrado el socio con número de cedula: {}".format(ciSocio)
            messageStrEmpty = "Debe ingersar un número de cedula para iniciar con la busqueda"
            self.view.mostrarPopup("Información", "Detalle", messageNotFount if ciSocio is not '' else messageStrEmpty)
    
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        width = (screen.width()-screen.width()/8)
        height = (screen.height()-screen.height()/8)
        self.window.setGeometry( (screen.width()-width) /2, (screen.height()-height)/2, width, height)

    def nextPage(self):
        if self.totalPartner == 0:
            return
        pageAmount = math.ceil(self.totalPartner/self.quantityElements)

        if self.actualPage < pageAmount:
            self.view.socioView = Socio(self.view, self.actualPage + 1)
            self.view.socioView.start()

    def previousPage(self):
        if self.actualPage > 1:
            self.view.socioView = Socio(self.view, self.actualPage -1)
            self.view.socioView.start()

    def firstPage(self):
        self.view.socioView = Socio(self.view, 1)
        self.view.socioView.start()

    def lastPage(self):
        if self.totalPartner <= 0:
            return
        pageAmount = math.ceil(self.totalPartner/self.quantityElements)

        self.view.socioView = Socio(self.view, pageAmount)
        self.view.socioView.start()

    def setState(self, socio):
        for s in socio:
            s.estado = "Activo" if s.estado else "Inactivo"
        return socio
