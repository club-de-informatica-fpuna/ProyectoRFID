from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from entidad.Carrera import Carrera
from functools import partial

class Carreras:

    def __init__(self, view):
        self.view = view
        self.carreras = self.view.generalController.carreraController.listarCarreras()

    def constriur(self):
        self.widget = QWidget()

        layout = QVBoxLayout()
        layoutButtons = QHBoxLayout()

        self.inputSearch = QLineEdit(self.widget)
        self.inputSearch.setObjectName("inputSearch")
        self.inputSearch.setPlaceholderText("Ingrese el nombre de la carrera")
        self.inputSearch.setMaximumWidth(500)

        btnNuevo = QPushButton("Registrar")
        btnNuevo.setObjectName("botonPrimario")
        btnNuevo.setIcon(QIcon("./view/resources/add.svg"))
        btnNuevo.clicked.connect(partial(self.registrarCarrera, None))

        shortcutNuevo = QShortcut(QKeySequence(Qt.Key_Return), btnNuevo)
        shortcutNuevo.setContext(Qt.WidgetShortcut)
        #shortcutNuevo.activated.connect(self.view.mostrarFormAlumno)

        btnEliminar = QPushButton("Eliminar")
        btnEliminar.setObjectName("cancel")
        btnEliminar.setIcon(QIcon("./view/resources/delete.svg"))
        btnEliminar.clicked.connect(partial(self.eliminarCarrera, None)) 

        shortcutEliminar = QShortcut(QKeySequence(Qt.Key_Return), btnEliminar)
        shortcutEliminar.setContext(Qt.WidgetShortcut)
        #shortcutEliminar.activated.connect(self.deleteStudents)                

        btnEditar = QPushButton("Editar")
        btnEditar.setObjectName("botonSecundario")
        btnEditar.setIcon(QIcon("./view/resources/edit.svg"))
        #btnEditar.clicked.connect(self.view.test)

        shortcutEditar = QShortcut(QKeySequence(Qt.Key_Return), btnEditar)
        shortcutEditar.setContext(Qt.WidgetShortcut)
        #shortcutEditar.activated.connect(self.manejarEditar)          

        self.listCarreras = QListWidget()
        for i in self.carreras:
            item = QListWidgetItem(i.denominacion)
            item.setData(Qt.UserRole, int(i.id))
            self.listCarreras.addItem(item)
        self.listCarreras.setObjectName("list")

        with open('./view/resources/styles.css') as f:
            btnEditar.setStyleSheet(f.read())        
        with open('./view/resources/styles.css') as f:
            btnNuevo.setStyleSheet(f.read())  
        with open('./view/resources/styles.css') as f:
            btnEliminar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            self.listCarreras.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            self.inputSearch.setStyleSheet(f.read())            

        layoutButtons.addStretch()
        layoutButtons.addWidget(self.inputSearch)        
        layoutButtons.addWidget(btnNuevo)
        layoutButtons.addWidget(btnEditar)
        layoutButtons.addWidget(btnEliminar)

        layout.addLayout(layoutButtons)
        layout.addWidget(self.listCarreras)
        
        layout.setContentsMargins(20,20,20,20)

        self.widget.setLayout(layout)
    
    def getWidgetBuilded(self):
        self.constriur()
        return self.widget

    def registrarCarrera(self, element):
        carreraDenominacion = self.inputSearch.text()
        if not carreraDenominacion :
            self.view.mostrarPopup("Validar", "Validar campos", "Por favor, complete el campo")
        else:
            carrera = Carrera()
            carrera.denominacion = carreraDenominacion
            res = self.view.generalController.carreraController.registrarCarrera(carrera)
            if res:
                self.view.mostrarConfiguracion()
            else:
                self.view.mostrarPopup("Error", "Ha ocurrido un error", "Ha ocurrido un error al crear el registro")

    def eliminarCarrera(self, element):
        selectedItems = self.listCarreras.currentItem()
        if selectedItems is None:
            self.view.mostrarPopup("Atención", "Atención", "Debes seleccionar el elemento a eliminar")                                   
            return
        idCarrera = selectedItems.data(Qt.UserRole)
        qm = QMessageBox
        ret = qm.question(self.widget,"Confirmación", "¿Desea eliminar los registros seleccionados?", qm.Yes | qm.No)
        if ret == qm.Yes:
            res = self.view.generalController.carreraController.eliminarCarrera(idCarrera)
            if res is True:
                self.view.mostrarConfiguracion()
            else:
                self.view.mostrarPopup("Atención", "No se puede eliminar", "Ha ocurrido un error al eliminar el registro")                        