from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from entidad.Alumno import Alumno
import os

class FormAlumno:

    def __init__(self, view, title, update=False, alumnoUpdate=None):
        self.view = view
        self.title = title
        self.update = update
        self.alumnoUpdate = alumnoUpdate
    
    def build(self):
        self.window = QWidget()
        self.window.setWindowTitle(self.title)
        self.carreras = self.view.generalController.carreraController.listarCarreras()
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

        self.inputNombre = QLineEdit()
        self.inputApellido = QLineEdit()
        self.inputCedula = QLineEdit()
        self.inputEmail = QLineEdit()
        self.inputTelefono = QLineEdit()
        self.inputCarreras = QComboBox()
        self.inputCarreras.addItem(" - Seleccione carrera - ")
        for i in self.carreras:
            self.inputCarreras.addItem(i.denominacion, i)

        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setObjectName("botonPrimario")        
        btnRegistrar.clicked.connect(self.manejarPostAlumno)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("botonPrimario")
        btnCancelar.clicked.connect(self.manejarCancelar)

        with open('./view/resources/styles.css') as f:
            btnCancelar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnRegistrar.setStyleSheet(f.read())


        horizontalLayout.addWidget(btnRegistrar)
        horizontalLayout.addWidget(btnCancelar)

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
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())

    def createGridUpdateLayout(self):

        self.layout = QGridLayout(self.window)
        horizontalLayout = QHBoxLayout()

        labelNombre = QLabel("Nombre")
        labelApellido = QLabel("Apellido")
        labelCedula = QLabel("Cedula de identidad")
        labelEmail = QLabel("Email")        
        labelTelefono = QLabel("Teléfono")
        labelCarreras = QLabel("Carrera")

        self.inputNombre = QLineEdit()
        self.inputNombre.setText(self.alumnoUpdate.nombre)

        self.inputApellido = QLineEdit()
        self.inputApellido.setText(self.alumnoUpdate.apellido)

        self.inputCedula = QLineEdit()        
        self.inputCedula.setEnabled(False)
        self.inputCedula.setText(self.alumnoUpdate.ci)

        self.inputEmail = QLineEdit()
        self.inputEmail.setText(self.alumnoUpdate.email)

        self.inputTelefono = QLineEdit()
        self.inputTelefono.setText(self.alumnoUpdate.telefono)

        self.inputCarreras = QComboBox()
        for i in self.carreras:
            self.inputCarreras.addItem(i.denominacion, i)
        self.inputCarreras.setCurrentIndex(0) 

        btnGuardar = QPushButton("Guardar")
        btnGuardar.setObjectName("botonPrimario")        
        #btnGuardar.clicked.connect(self.manejarPostAlumno)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setObjectName("botonPrimario")
        btnCancelar.clicked.connect(self.manejarCancelar)

        with open('./view/resources/styles.css') as f:
            btnCancelar.setStyleSheet(f.read())
        with open('./view/resources/styles.css') as f:
            btnGuardar.setStyleSheet(f.read())

        horizontalLayout.addWidget(btnGuardar)
        horizontalLayout.addWidget(btnCancelar)

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
        with open('./view/resources/styles.css') as f:
            self.window.setStyleSheet(f.read())            

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