from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from entidad.Alumno import Alumno
import os

class FormAlumno:

    def __init__(self, view, title, update=False, alumnoUpdate=None, editable=True, raceById=None):
        self.view         = view
        self.title        = title
        self.update       = update
        self.alumnoUpdate = alumnoUpdate
        self.editable     = editable
        self.raceById     = raceById
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.carreras = self.view.generalController.carreraController.listarCarreras()
        self.pathResources  = "./view/resources/"
        self.pathIcons      = "./view/resources/icons/"

        if self.update:
            self.createGridUpdateLayout()            
        else:
            self.createGridLayout()
        self.center()

    def start(self):
        self.build()
        self.window.show()

    def createGridLayout(self):

        self.layout = QGridLayout(self.window)
        horizontalLayout = QHBoxLayout()

        labelNombre = QLabel("Nombre")
        labelApellido = QLabel("Apellido")
        labelCedula = QLabel("Cedula de identidad")
        labelEmail = QLabel("Email")        
        labelTelefono = QLabel("Teléfono")
        labelCarreras = QLabel("Carrera")

        self.inputNombre = QLineEdit(self.window)
        self.inputNombre.setObjectName("inputFormEnable")
        self.inputNombre.setFocus()
        self.inputApellido = QLineEdit(self.window)
        self.inputApellido.setObjectName("inputFormEnable")
        self.inputCedula = QLineEdit(self.window)
        self.inputCedula.setObjectName("inputFormEnable")
        self.inputEmail = QLineEdit(self.window)
        self.inputEmail.setObjectName("inputFormEnable")
        self.inputTelefono = QLineEdit(self.window)
        self.inputTelefono.setObjectName("inputFormEnable")
        self.inputCarreras = QComboBox(self.window)
        self.inputCarreras.setObjectName("inputSelect")
        self.inputCarreras.addItem(" - Seleccione carrera - ")
        for i in self.carreras:
            self.inputCarreras.addItem(i.denominacion, i)            

        shortcutCarreras = QShortcut(QKeySequence(Qt.Key_Return), self.inputCarreras)
        shortcutCarreras.setContext(Qt.WidgetShortcut)
        shortcutCarreras.activated.connect(self.manejarPostAlumno)

        shortcutTelefono = QShortcut(QKeySequence(Qt.Key_Return), self.inputTelefono)
        shortcutTelefono.setContext(Qt.WidgetShortcut)
        shortcutTelefono.activated.connect(self.inputCarreras.setFocus)        

        shortcutEmail = QShortcut(QKeySequence(Qt.Key_Return), self.inputEmail)
        shortcutEmail.setContext(Qt.WidgetShortcut)
        shortcutEmail.activated.connect(self.inputTelefono.setFocus)

        shortcutCedula = QShortcut(QKeySequence(Qt.Key_Return), self.inputCedula)
        shortcutCedula.setContext(Qt.WidgetShortcut)
        shortcutCedula.activated.connect(self.inputEmail.setFocus)        

        shortcutApellido = QShortcut(QKeySequence(Qt.Key_Return), self.inputApellido)
        shortcutApellido.setContext(Qt.WidgetShortcut)
        shortcutApellido.activated.connect(self.inputCedula.setFocus)        

        shortcutNombre = QShortcut(QKeySequence(Qt.Key_Return), self.inputNombre)
        shortcutNombre.setContext(Qt.WidgetShortcut)
        shortcutNombre.activated.connect(self.inputApellido.setFocus)

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setObjectName("botonPrimario")
        btnRegistrar.setIcon(QIcon(self.pathIcons + "floppy.png"))
        btnRegistrar.clicked.connect(self.manejarPostAlumno)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("cancel")
        btnCancelar.setIcon(QIcon(self.pathIcons + "cancel.png"))
        btnCancelar.clicked.connect(self.manejarCancelar)

        with open(self.pathResources + "styles.css") as f:
            btnCancelar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            btnRegistrar.setStyleSheet(f.read())

        horizontalLayout.addWidget(btnRegistrar)
        horizontalLayout.addWidget(btnCancelar)

        horizontalLayout.setContentsMargins(0,20,0,0)

        self.layout.addWidget(labelNombre,0,0,1,2)
        self.layout.addWidget(self.inputNombre,1,0,1,2)
        self.layout.addWidget(labelApellido,2,0,1,2)        
        self.layout.addWidget(self.inputApellido,3,0,1,2)        
        self.layout.addWidget(labelCedula,4,0,1,2)        
        self.layout.addWidget(self.inputCedula,5,0,1,2)  
        self.layout.addWidget(labelEmail,6,0,1,2)        
        self.layout.addWidget(self.inputEmail,7,0,1,2)                        
        self.layout.addWidget(labelTelefono,8,0,1,2)        
        self.layout.addWidget(self.inputTelefono,9,0,1,2)
        self.layout.addWidget(labelCarreras,10,0,1,2)        
        self.layout.addWidget(self.inputCarreras,11,0,1,2)
        self.layout.addLayout(horizontalLayout,12,0,1,2)

        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaPopup")
        with open(self.pathResources + "styles.css") as f:
            self.window.setStyleSheet(f.read())

        shortcutSalir = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcutSalir.setContext(Qt.WindowShortcut)
        shortcutSalir.activated.connect(self.window.hide)            

    def createGridUpdateLayout(self):

        self.layout = QGridLayout(self.window)
        horizontalLayout = QHBoxLayout()

        labelNombre = QLabel("Nombre")
        labelApellido = QLabel("Apellido")
        labelCedula = QLabel("Cedula de identidad")
        labelEmail = QLabel("Email")        
        labelTelefono = QLabel("Teléfono")
        labelCarreras = QLabel("Carrera")

        self.inputCarreras = QComboBox(self.window)
        self.inputCarreras.setObjectName("inputSelect")
        for i in self.carreras:
            self.inputCarreras.addItem(i.denominacion, i)
        careerIndex = self.inputCarreras.findText(self.raceById.denominacion)
        self.inputCarreras.setCurrentIndex(careerIndex)

        shortcutCarreras = QShortcut(QKeySequence(Qt.Key_Return), self.inputCarreras)
        shortcutCarreras.setContext(Qt.WidgetShortcut)
        shortcutCarreras.activated.connect(self.manejarUpdateAlumno)        

        self.inputTelefono = QLineEdit(self.window)
        self.inputTelefono.setObjectName("inputFormEnable")
        self.inputTelefono.setText(self.alumnoUpdate.telefono)

        shortcutTelefono = QShortcut(QKeySequence(Qt.Key_Return), self.inputTelefono)
        shortcutTelefono.setContext(Qt.WidgetShortcut)
        shortcutTelefono.activated.connect(self.inputCarreras.setFocus)           

        self.inputEmail = QLineEdit(self.window)
        self.inputEmail.setObjectName("inputFormEnable")
        self.inputEmail.setText(self.alumnoUpdate.email)

        shortcutEmail = QShortcut(QKeySequence(Qt.Key_Return), self.inputEmail)
        shortcutEmail.setContext(Qt.WidgetShortcut)
        shortcutEmail.activated.connect(self.inputTelefono.setFocus)

        self.inputCedula = QLineEdit(self.window)
        self.inputCedula.setObjectName("inputFormDisable")
        self.inputCedula.setEnabled(False)
        self.inputCedula.setText(self.alumnoUpdate.ci)

        self.inputApellido = QLineEdit(self.window)
        self.inputApellido.setObjectName("inputFormEnable")
        self.inputApellido.setText(self.alumnoUpdate.apellido)

        shortcutApellido = QShortcut(QKeySequence(Qt.Key_Return), self.inputApellido)
        shortcutApellido.setContext(Qt.WidgetShortcut)
        shortcutApellido.activated.connect(self.inputEmail.setFocus)        

        self.inputNombre = QLineEdit(self.window)
        self.inputNombre.setObjectName("inputFormEnable")
        self.inputNombre.setText(self.alumnoUpdate.nombre)
        self.inputNombre.setFocus()

        shortcutNombre = QShortcut(QKeySequence(Qt.Key_Return), self.inputNombre)
        shortcutNombre.setContext(Qt.WidgetShortcut)
        shortcutNombre.activated.connect(self.inputApellido.setFocus)

        if self.editable is False:
            self.inputNombre.setEnabled(False)
            self.inputApellido.setEnabled(False)
            self.inputCedula.setEnabled(False)
            self.inputEmail.setEnabled(False)
            self.inputTelefono.setEnabled(False)
            self.inputCarreras.setEnabled(False)

        btnGuardar = QPushButton("Actualizar")
        btnGuardar.setObjectName("botonPrimario")
        btnGuardar.setIcon(QIcon(self.pathIcons + "update.png"))
        btnGuardar.clicked.connect(self.manejarUpdateAlumno)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("cancel")
        btnCancelar.setIcon(QIcon(self.pathIcons + "cancel.png"))
        btnCancelar.clicked.connect(self.manejarCancelar)

        btnCerrar = QPushButton("Cerrar")
        btnCerrar.setObjectName("botonPrimario")
        btnCerrar.setIcon(QIcon(self.pathIcons + "cancel.png"))
        btnCerrar.clicked.connect(self.manejarCancelar)

        with open(self.pathResources + "styles.css") as f:
            btnCancelar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            btnGuardar.setStyleSheet(f.read())
        with open(self.pathResources + "styles.css") as f:
            btnCerrar.setStyleSheet(f.read())            

        if self.editable is True:
            horizontalLayout.addWidget(btnGuardar)
            horizontalLayout.addWidget(btnCancelar)
        else:
            shortcutCerrar = QShortcut(QKeySequence(Qt.Key_Return), btnCerrar)
            shortcutCerrar.setContext(Qt.WidgetShortcut)
            shortcutCerrar.activated.connect(self.window.hide)  
            horizontalLayout.addWidget(btnCerrar)
        
        horizontalLayout.setContentsMargins(0,20,0,0)

        self.layout.addWidget(labelNombre,0,0,1,2)
        self.layout.addWidget(self.inputNombre,1,0,1,2)
        self.layout.addWidget(labelApellido,2,0,1,2)        
        self.layout.addWidget(self.inputApellido,3,0,1,2)        
        self.layout.addWidget(labelCedula,4,0,1,2)        
        self.layout.addWidget(self.inputCedula,5,0,1,2)  
        self.layout.addWidget(labelEmail,6,0,1,2)        
        self.layout.addWidget(self.inputEmail,7,0,1,2)                        
        self.layout.addWidget(labelTelefono,8,0,1,2)        
        self.layout.addWidget(self.inputTelefono,9,0,1,2)
        self.layout.addWidget(labelCarreras,10,0,1,2)        
        self.layout.addWidget(self.inputCarreras,11,0,1,2)
        self.layout.addLayout(horizontalLayout,12,0,1,2)

        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.window.setObjectName("ventanaPopup")
        with open(self.pathResources + "styles.css") as f:
            self.window.setStyleSheet(f.read())

        shortcutSalir = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcutSalir.setContext(Qt.WindowShortcut)
        shortcutSalir.activated.connect(self.window.hide)            

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.window.geometry()      
        self.window.move((screen.width() - size.width()) /2, (screen.height() - size.height()) / 2)
    
    def manejarPostAlumno(self):
        alumno = Alumno()
        alumno.ci = self.inputCedula.text()
        alumno.nombre = self.inputNombre.text()
        alumno.apellido = self.inputApellido.text()
        alumno.telefono = self.inputTelefono.text()
        alumno.email = self.inputEmail.text()
        carrera = self.inputCarreras.currentData()
        if carrera is None:
            alumno.idCarrera = None
        else:
            alumno.idCarrera = carrera.id
        resValidacion = self.validarCampos(alumno)
        if resValidacion is not True:
            self.view.mostrarPopup("Validar campos", "Por favor, verifique los siguientes campos", resValidacion)
            return

        res = self.view.generalController.alumnoController.registrarAlumno(alumno)
        if res is True:
            self.window.destroy()
            self.view.mostrarModuloAlumnos()
        else:
            self.view.mostrarPopup("Error", "Ha ocurrido un error", res)

    def manejarUpdateAlumno(self):
        alumno = Alumno()
        alumno.ci = self.inputCedula.text()
        alumno.nombre = self.inputNombre.text()
        alumno.apellido = self.inputApellido.text()
        alumno.telefono = self.inputTelefono.text()
        alumno.email = self.inputEmail.text()
        carrera = self.inputCarreras.currentData()
        if carrera is None:
            alumno.idCarrera = None
        else:
            alumno.idCarrera = carrera.id
        resValidacion = self.validarCampos(alumno)
        if resValidacion is not True:
            self.view.mostrarPopup("Validar campos", "Por favor, verifique los siguientes campos", resValidacion)
            return
        res = self.view.generalController.alumnoController.actualizarAlumnos(alumno)
        if res is True:
            self.window.destroy()
            self.view.mostrarModuloAlumnos()
        else:
            self.view.mostrarPopup("Error", "Ha ocurrido un error", res)            
    
    def manejarCancelar(self):
        self.window.hide()

    def validarCampos(self, alumno):
        campos = []
        if not alumno.nombre :
            campos.append("Nombre")
        if not alumno.apellido:
            campos.append("Apellido")
        if not alumno.telefono:
            campos.append("Teléfono")
        if not alumno.email:
            print(alumno.email)
            campos.append("Email")                                   
        try:
            ciNumber = int(alumno.ci)
        except(Exception) as error:
            campos.append("Cédula de identidad")
        if alumno.idCarrera is None:
            campos.append("Carrera")        
        if len(campos) > 0:
            return campos
        else:
            return True